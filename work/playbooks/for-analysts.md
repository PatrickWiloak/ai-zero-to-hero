# AI for Analysts

**In one line:** Use AI to write and explain formulas, SQL and Python, clean messy data, and draft the narrative around your findings - but have it produce code you run, not numbers you trust, so every result is reproducible and checkable.
**Last reviewed:** 2026-10-21

---

## The short version

- The single most important habit: **ask for the method, not the answer.** "Write the SQL / formula / pandas code that computes X" is checkable. "What is the average of this table?" is not.
- Language models can make arithmetic and counting mistakes when they work "in their head". Tools that run code (data analysis features in the major assistants, notebooks) are much more reliable, but you still check the code.
- Great uses: writing and debugging formulas, SQL and Python; explaining an unfamiliar query or spreadsheet; data cleaning logic; drafting commentary; brainstorming hypotheses and checks.
- Weak uses: anything where you cannot verify the result, and conclusions about causation.
- Data rules matter more for you than for most roles, because your inputs are often customer or financial data. Use approved tools and paste schemas and samples, not full datasets, unless your tool and policy allow it.

## Why "show me the code" beats "tell me the number"

A language model generates text token by token. It can produce a plausible-looking total that is wrong, especially across many rows, and it will not tell you. When the assistant writes and runs code instead, the arithmetic is done by the computer, and you can read exactly what it did.

So the workflow is:

```
1. Describe the data (schema + a few sample rows, no restricted data)
2. Ask for code (SQL / Excel formula / Python) that answers the question
3. Read the code. Ask it to explain anything you do not follow.
4. Run it yourself on the real data, in your normal environment
5. Sanity-check the result (totals, row counts, a hand-computed example)
6. Ask AI to help draft the narrative, from YOUR verified numbers
```

## Copyable prompts

**Write a query from a schema**
```
Database: [Postgres/Snowflake/BigQuery]. Tables:
orders(order_id, customer_id, order_date, status, amount_usd)
customers(customer_id, signup_date, region, segment)

Write SQL for: monthly revenue by region for the last 12 full months,
excluding status = 'refunded', with month-over-month % change.
Explain each step in a comment. Point out any assumptions (time zones,
partial months, nulls).
```

**Explain something you inherited**
```
Explain what this [SQL / Excel formula / Python] does, step by step, in
plain language. Then list anything that looks like a bug or a fragile
assumption: [paste].
```

**Excel or Sheets formula**
```
In Google Sheets, column A has dates, column B has customer IDs, column C
has amounts. Write a formula for F2 that gives the number of distinct
customers who bought in the month shown in E2 (E2 is the first of the
month). Explain how it works and how to test it on a small example.
```

**Data cleaning plan**
```
Here are 20 sample rows from a messy CSV export [paste, with personal data
replaced by fake values]. List every data quality issue you see (formats,
duplicates, inconsistent categories, nulls). Then write pandas code that
fixes them and prints a before/after count for each fix.
```

**Hypotheses and checks**
```
Our trial-to-paid conversion fell from [x]% to [y]% between [month] and
[month]. Here is what changed in that period: [list]. Give me 8 hypotheses,
and for each the specific query or cut of the data that would confirm or
rule it out. Rank by how cheap they are to check.
```

**Commentary from verified numbers**
```
Here are the verified results: [paste table]. Write a 150-word summary for
[audience] covering the 3 most important movements. Use only these numbers.
Do not imply causes unless I state them: [list known causes].
```

## Before and after

**Before.** An analyst needs to answer "which regions are driving the revenue drop?" She spends an hour writing a window-function query from memory and Stack Overflow, another 30 minutes debugging a partial-month issue, then an hour writing the commentary.

**After.** She pastes the schema and the question into the query prompt and gets a working draft in a minute, which already flags the partial-month problem. She reads it, fixes one join, runs it, and checks the total against the finance dashboard. She asks for three alternative cuts of the data, runs two of them, and writes the commentary from a draft built only on her verified table. The work takes about half the time, and the "assumptions" list from the AI catches a time-zone issue she would have missed.

She did not paste the customer table into the chat, and she did not take any number from the AI's prose.

## Using built-in data analysis features

The major assistants can now take an uploaded file and run code on it in a sandbox. This is useful for exploration and charts, with conditions:

- **Check whether your policy allows uploading that file.** Uploading a full customer export to a tool not approved for Restricted data breaks most policies.
- **Open the code.** Every reputable tool lets you see the code it ran. Read it; that is your audit trail.
- **Re-run important results** in your own environment before they go in a report.
- **Watch for silent assumptions**: dropped rows with nulls, date parsing, duplicated joins.

## Where not to use it

- **Final numbers in reports** that came from the model's prose rather than executed code.
- **Causal claims.** AI will happily explain why a number moved. That is a hypothesis, not a finding.
- **Statistics you cannot validate.** If it suggests a test you do not understand, learn it or ask a statistician before reporting results.
- **Restricted data** in unapproved tools. Use schemas, synthetic samples or aggregated data.

## Failure modes

- **Plausible wrong SQL.** Joins that duplicate rows, filters in the wrong place, off-by-one dates. Always check row counts and a known total.
- **Hallucinated functions.** A function that exists in one SQL dialect but not yours, or a spreadsheet function that does not exist. Say which dialect and version.
- **Overconfident narrative.** Smooth commentary that overstates certainty. Edit it down.
- **Lost reproducibility.** A chat transcript is not a pipeline. Save the final code in your repository or workbook.

## Common mistakes

- Pasting raw data and asking for an answer.
- Not saying which tool, dialect or version you use.
- Accepting the first query without reading it.
- Using AI to skip learning the basics. You need enough SQL and statistics to spot a wrong answer.

## Next steps

- Digging through documents and sources: [research and analysis](../use-cases/research-and-analysis.md)
- Turning documents into structured data: [document processing](../use-cases/document-processing.md)
- If you want to automate this into a pipeline: [structured outputs](../../learn/concepts/structured-outputs.md) and [structured extraction pipeline](../../build/projects/structured-extraction-pipeline.md)
- Learn the Python basics: [Python for AI](../../learn/day-one/python-for-ai.md)
- Why models struggle with arithmetic on text: [tokenization](../../explainers/concepts/tokenization.md)

## Sources

- OpenAI, *Data analysis with ChatGPT* (example of an assistant that writes and runs Python in a sandbox on uploaded files; other assistants offer similar features - check your tool's documentation): <https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt>
