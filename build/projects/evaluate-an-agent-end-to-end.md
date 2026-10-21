# Evaluate an Agent End to End

**In one line:** Measure an agent the way it will be used: a fixed set of realistic tasks, several trials each, graded on the final state of the world (not on what the agent says), with success rate, consistency, cost per success and cheating checks in one report you can rerun after every change.
**Last reviewed:** 2026-10-21

---

## The short version

- Grading a single model answer is the job of [Set up an eval harness](set-up-eval-harness.md). An **agent** eval is different: the agent takes many steps, uses tools, changes things, and can succeed or fail in ways its final message does not reveal.
- Grade **outcomes**: after each run, inspect the environment (do the hidden tests pass? is the database row correct? was the email actually not sent?). Never grade the agent's own summary.
- Run each task **several times**. Agents are non-deterministic; a task solved one time in three is not solved. Report both "solved at least once" and "solved every time".
- Track **cost, steps and time per successful task**, and **guardrail violations** (here: edits to the existing tests, the coding agent's favourite shortcut).
- You will build a ~90-line harness that runs the coding agent from [Build a coding agent loop](build-a-coding-agent-loop.md) over a folder of tasks, each in a fresh copy, and writes `results.csv` plus a summary. Time: 1 to 2 hours, plus API cost for the runs (tasks x trials x cost per run; estimate it first with [AI cost basics](../../learn/concepts/ai-cost-basics.md)).

## What makes agent evals different

| | Single-call eval | Agent eval |
|---|---|---|
| Unit | One prompt, one answer | One task, many steps |
| What you grade | The text | The end state of an environment, plus the path taken |
| Variance | Moderate (temperature) | High: small early differences compound over steps |
| Cost per case | Cents or less | Often 10 to 100 times more |
| Typical failure | Wrong or badly formatted answer | Gives up, loops, does the wrong thing confidently, "succeeds" by cheating |

Public agent benchmarks follow the same design. [SWE-bench](../../papers/techniques/84-swe-bench/summary.md) grades a patch by running the project's tests; [OSWorld](../../papers/techniques/139-osworld/summary.md) grades by a script that inspects the machine's final state; τ-bench (Yao et al., 2024) introduced **pass^k**, the chance an agent succeeds on all k independent tries, because a customer-service agent that works two times in three is not one you can deploy. Your own eval should look like a tiny version of these, built from your tasks.

## Step 1: design the tasks

Each task is a folder:

```
tasks/
  cart-discount/
    task.json        {"prompt": "...", "timeout": 600}
    repo/            the starting state the agent works on (code + visible tests)
    hidden_test.py   the grader: run after the agent finishes, never shown to it
  slugify/
    ...
```

Guidelines:

- **Realistic and varied.** Take tasks from your real backlog: bug fixes, small features, refactors. Mix easy and hard. Twenty to fifty tasks is a solid start; ten is enough to begin.
- **Unambiguous success.** If two engineers would disagree on whether the result is correct, the task needs a sharper prompt or a better grader.
- **Hidden graders.** Visible tests tell the agent what to aim for; hidden tests check it did not overfit to them. They also catch the agent special-casing the visible test inputs.
- **Solvable.** Check every task by solving it yourself (or confirming a known fix passes the hidden test). A task nobody can pass measures nothing.
- **Fresh state every run.** Copy the starting folder for each trial so runs cannot affect each other.

Two example tasks. The first reuses the shop project from the coding-agent page; its `hidden_test.py`:

```python
from cart import total

def test_threshold_exact():
    assert total([(2500, 2)], "SAVE10") == 4500

def test_below_threshold_no_discount():
    assert total([(4999, 1)], "SAVE10") == 4999

def test_result_is_int():
    assert isinstance(total([(3333, 3)], "SAVE10"), int)
```

The second asks for a feature: `repo/text.py` has `slugify(title)` returning `title.lower().replace(" ", "-")`, with a docstring saying only `a-z` and `0-9` are kept and words are joined by single hyphens. The prompt is "slugify() should match its docstring: punctuation removed and runs of spaces collapsed. Fix it and add tests." The hidden test checks `slugify("What's New, 2026?") == "whats-new-2026"` and `slugify("  many   spaces ") == "many-spaces"`.

## Step 2: the harness

Save as `run_eval.py` next to `agent.py` and `tasks/`:

```python
"""Run an agent over a folder of tasks, several trials each, and grade every run."""
import csv, hashlib, json, re, shutil, statistics, subprocess, sys, tempfile, time
from pathlib import Path

TASKS = Path("tasks")
TRIALS = 3                     # agents are non-deterministic: run each task more than once
AGENT = [sys.executable, "agent.py"]   # called as: agent.py <workdir> <prompt>
PRICE_IN, PRICE_OUT = 4.00, 20.00      # USD per million tokens for the model the agent uses

def digest(folder: Path) -> dict:
    return {str(p.relative_to(folder)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob("test_*.py")}

def run_one(task_dir: Path, trial: int) -> dict:
    spec = json.loads((task_dir / "task.json").read_text())
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "repo"
        shutil.copytree(task_dir / "repo", work)          # fresh copy every trial
        before = digest(work)
        start = time.time()
        try:
            proc = subprocess.run(AGENT + [str(work), spec["prompt"]], capture_output=True,
                                  text=True, timeout=spec.get("timeout", 600))
            log, timed_out = proc.stdout + proc.stderr, False
        except subprocess.TimeoutExpired as exc:
            log, timed_out = (exc.stdout or b"").decode(errors="replace"), True
        seconds = time.time() - start

        # Grade on the final state of the files, never on what the agent says it did.
        after = digest(work)       # new test files are fine; changed existing ones are not
        tests_untouched = all(after.get(name) == h for name, h in before.items())
        shutil.copy(task_dir / "hidden_test.py", work / "test_hidden_grader.py")
        graded = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
                                cwd=work, capture_output=True, text=True, timeout=300)
        tests_pass = graded.returncode == 0

    tokens_in = sum(int(n) for n in re.findall(r"in=(\d+)", log))
    tokens_out = sum(int(n) for n in re.findall(r"out=(\d+)", log))
    return {
        "task": task_dir.name, "trial": trial,
        "success": tests_pass and tests_untouched and not timed_out,
        "tests_pass": tests_pass, "tests_untouched": tests_untouched, "timed_out": timed_out,
        "steps": log.count("--- step"), "seconds": round(seconds, 1),
        "cost_usd": round((tokens_in * PRICE_IN + tokens_out * PRICE_OUT) / 1e6, 4),
    }

def main() -> None:
    rows = [run_one(t, k) for t in sorted(p for p in TASKS.iterdir() if p.is_dir())
            for k in range(1, TRIALS + 1)]
    with open("results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    by_task = {}
    for r in rows:
        by_task.setdefault(r["task"], []).append(r["success"])
    successes = [r for r in rows if r["success"]]
    total_cost = sum(r["cost_usd"] for r in rows)
    print(f"{'task':<24} trials  passed")
    for task, results in by_task.items():
        print(f"{task:<24} {len(results):>6}  {sum(results):>6}")
    print(f"\nsuccess rate (all trials): {len(successes) / len(rows):.0%}")
    print(f"tasks solved every trial:  {sum(all(v) for v in by_task.values())}/{len(by_task)}")
    print(f"tasks solved at least once: {sum(any(v) for v in by_task.values())}/{len(by_task)}")
    print(f"tests edited (cheating?):  {sum(not r['tests_untouched'] for r in rows)} runs")
    print(f"median steps: {statistics.median(r['steps'] for r in rows)}  "
          f"median seconds: {statistics.median(r['seconds'] for r in rows)}")
    if successes:
        print(f"cost per successful run: ${total_cost / len(successes):.3f}  (total ${total_cost:.2f})")

if __name__ == "__main__":
    main()
```

Design choices worth noticing:

- **The agent runs as a subprocess** with a timeout, so a hung or crashing agent is recorded as a failure instead of killing the eval. Any agent that takes `<workdir> <prompt>` can be plugged in, so you can compare harnesses, models or prompts on the same tasks.
- **Grading happens after the agent exits**, on the files it left behind, by copying in the hidden test. The agent's final message is never read.
- **The cheating check** hashes every existing `test_*.py` file before and after. Adding new tests is fine (the slugify task asks for it); changing existing ones fails the run.
- **Cost** is computed from the token counts the coding agent prints each step. Set `PRICE_IN` and `PRICE_OUT` to your model's prices (the defaults match Claude Opus 5.5 as listed by Anthropic on 2026-10-21). Better still, have your agent write usage to a file.
- **`results.csv`** keeps every run, so you can open it in a spreadsheet, and diff it against last week's.

## Step 3: run and read the report

```bash
python run_eval.py
```

The report has this shape (the numbers below come from a dry run of the harness with a scripted stand-in agent, to show the format; your real agent's numbers will differ):

```
task                     trials  passed
cart-discount                 3       3
slugify                       3       0

success rate (all trials): 50%
tasks solved every trial:  1/2
tasks solved at least once: 1/2
tests edited (cheating?):  3 runs
median steps: 2.0  median seconds: 0.0
cost per successful run: $0.066  (total $0.20)
```

How to read it:

- **Success rate across all trials** is your headline number. Track it over time.
- **Solved every trial versus at least once** is the consistency gap. A large gap means the agent can do the task but not reliably: look at what differs between its good and bad runs.
- **Any "tests edited" count above zero needs a look.** In this dry run the stand-in agent "solved" slugify by weakening the visible test, and the harness caught it: the hidden test failed and the edit was flagged.
- **Cost per successful run** is the number to compare against a human doing the task. Failed runs still cost money, so divide total cost by successes, not by runs.

## Step 4: look at transcripts, then change one thing

Numbers say how often; transcripts say why. For each failing task, save the agent's log (extend `run_one` to write `log` to `runs/<task>-<trial>.txt`) and read a few. Typical patterns and fixes:

| You see | Likely fix |
|---|---|
| Edits fail with "found 0 times" repeatedly | The agent edits from memory; tell it to re-read before editing, or return the current file content in the error |
| Stops before running the tests | Strengthen the system prompt ("never finish without a passing test run") or check in the loop |
| Loops on the same failure | Add a hint when the same tool result repeats; cap steps lower |
| Fixes the visible test case only | Hidden tests already catch this; add to the prompt that tests are examples, not the spec |
| Runs out of context on big files | Paginate `read_file`, add a search tool |

Then change **one** thing (the prompt, a tool description, the model, the step limit), rerun everything, and compare. With only a few tasks, differences of one or two successes are noise; add tasks or trials before trusting a small change. If you want to grade the path as well as the outcome (did it read the right files, did it take a risky action?), add an **LLM judge** over the transcripts with a short rubric, and check its verdicts by hand on a sample first; see the [LLM-as-a-judge summary](../../papers/techniques/85-llm-as-judge/summary.md).

## Beyond coding agents

The same harness shape works for any agent; only the environment and the grader change:

| Agent | Starting state | Outcome grader |
|---|---|---|
| Support agent with tools | Seeded database of customers and orders | Query the database: was the right refund issued, and nothing else changed? |
| Research agent | A fixed document set or cached web pages | Exact-match or rubric check of the final answer against a reference |
| Computer-use agent | A VM snapshot | A script that inspects files, app state or settings, as OSWorld does |
| Email or calendar agent | A sandbox mailbox | Check what was sent, to whom, and that nothing was sent that should not have been |

Always include **negative tasks**: requests the agent should refuse or escalate (a refund above its limit, an instruction injected in a document). Success there means the action did **not** happen. See [Prompt injection red team](prompt-injection-red-team.md).

## Verification

- `results.csv` has one row per task per trial.
- A task you know is unsolvable (try an empty `repo/` with a hidden test) shows 0 passes, and a task where you hand the agent the answer shows full passes: the grader can tell the difference.
- Deliberately editing a visible test inside `agent.py` shows up in "tests edited".
- Rerunning without changes gives similar, not identical, numbers. That spread is your noise floor.

## Common mistakes

- **Trusting the agent's summary.** Only the environment's end state counts.
- **One trial per task.** You will mistake luck for capability, in both directions.
- **Graders the agent can see.** It will optimise for them. Keep the real checks hidden.
- **Shared state between runs.** A database or folder left dirty by one run changes the next.
- **Only measuring success.** Cost, time and violations decide whether you can ship it.
- **Tiny task sets with big conclusions.** Five tasks cannot separate two agents that differ by 10 points.

## Next steps

- [Build a coding agent loop](build-a-coding-agent-loop.md): the agent this harness runs
- [Set up an eval harness](set-up-eval-harness.md) and [Evals for LLMs](../../learn/concepts/evals-for-llms.md): single-call evals and CI gates
- [Training, validation and overfitting](../../learn/concepts/training-validation-and-overfitting.md): why your tuning tasks and your final check should differ
- [Agents and computer use benchmarks explainer](../../explainers/benchmarks/agents-and-computer-use.md) and [METR time horizons](../../papers/techniques/145-metr-time-horizons/summary.md)
- [LLMOps and observability](../patterns/llmops-observability.md): the production side of the same measurements

## Sources

- Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" (2023): https://arxiv.org/abs/2310.06770
- Yao et al., "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains" (2024), which defines pass^k: https://arxiv.org/abs/2406.12045
- Xie et al., "OSWorld" (2024): https://arxiv.org/abs/2404.07972
- Anthropic, "Building Effective Agents" (December 2024): https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, pricing (default prices in the harness), read 2026-10-21: https://platform.claude.com/docs/en/about-claude/pricing
- Tested on 2026-10-21: the harness was run end to end on the two tasks above with a scripted stand-in agent (including the test-editing check); it was not run against a live model for this page.
