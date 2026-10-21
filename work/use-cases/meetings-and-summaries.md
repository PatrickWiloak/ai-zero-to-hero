# Meetings and Summaries

**In one line:** Use AI to transcribe meetings and turn them into decisions, action items and short summaries - with everyone's knowledge and consent, a human checking owners and dates, and clear rules about what gets recorded and kept.
**Last reviewed:** 2026-10-21

---

## The short version

- AI note-taking is one of the fastest wins for most teams: transcription is now good, and turning a transcript into decisions and actions is a task language models do well.
- The two failure points are **consent** (recording people without telling them, which is illegal in some places) and **accuracy** (summaries that attribute the wrong decision or owner).
- Prefer the note-taker built into your approved meeting platform over third-party bots that join calls, unless IT has approved the bot.
- A good summary prompt asks for **decisions**, **actions with owners and dates**, and **open questions**, and tells the AI to write "not stated" rather than guess.
- Set retention rules. A searchable archive of every meeting is useful and also a liability.

## How it works

```
Audio -> speech-to-text (transcript with speaker labels)
      -> language model (summary, decisions, actions, follow-up email)
      -> human check -> shared notes / tasks in your tracker
```

Speech recognition took a large step forward with models trained on huge amounts of varied audio, such as OpenAI's [Whisper](../../papers/multimodal/49-whisper/summary.md). Transcripts are still imperfect with crosstalk, accents, jargon, names and poor microphones, and speaker labels are often the weakest part. Most summary errors start as transcript errors.

## Consent and privacy first

- **Tell people.** Announce recording at the start, in the invite, or both. Many platforms show a recording indicator, but do not rely on it alone, especially with external guests.
- **Know the law.** In the United States, some states, including California, Florida and Illinois, require the consent of every party to record a conversation. Other countries have their own rules, and data protection law (such as GDPR in Europe) treats recordings and transcripts of identifiable people as personal data.
- **Not every meeting should be recorded.** HR conversations, performance discussions, legal matters, sensitive negotiations and one-to-ones should default to no recording.
- **Third-party bots.** Note-taker bots that join meetings send audio to another vendor. They count as AI tools under your [acceptable use policy](../enablement/acceptable-use-policy.md) and need approval like any other.
- **Retention.** Decide how long recordings and transcripts are kept (for example, transcripts 90 days, summaries kept with the project), and set it in the tool.

## Copyable prompts

Use these with a transcript from an approved tool, or with your own notes.

**Standard meeting summary**
```
Here is a meeting transcript: [paste].
Produce:
1. Summary - 3 to 5 sentences: purpose and outcome.
2. Decisions - each with the speaker and a short exact quote that shows the
   decision was made. If something was discussed but not decided, it goes
   under Open questions, not here.
3. Action items - table: action, owner, due date. Write "not stated" for
   any owner or date not explicitly said. Do not assign owners yourself.
4. Open questions and risks.
Keep it under 300 words excluding the table.
```

**Follow-up email to attendees**
```
From the summary above, write a follow-up email to attendees. Subject line
with the meeting name and date. Thank-you in one line at most. Decisions,
then actions with owners, then next meeting. Plain, under 180 words.
```

**Catch-up for someone who missed it**
```
I missed this meeting. From the transcript [paste], tell me in under 150
words: what was decided that affects [my team / my project], anything I am
expected to do, and anything I should push back on.
```

**Series summary**
```
Here are summaries of the last 6 weekly meetings for [project]: [paste].
Track how each open issue evolved: when it was raised, what changed, current
status. List actions that have appeared in more than one meeting without
being closed.
```

## Before and after

**Before.** A project manager takes notes while running a weekly call with eight people, misses half of the discussion while typing, and sends notes the next day. People dispute who agreed to what.

**After.** The meeting platform's built-in transcription runs, announced at the start. Afterwards she runs the standard summary prompt, checks every owner and date against the transcript (two were "not stated", so she confirms them in the chat), and sends the follow-up within 20 minutes. She runs the meeting instead of typing. When a decision is disputed later, the summary quotes the line.

## Beyond meetings: summarising anything

The same techniques work for long email threads, chat channels, reports and documents:

- **Say who the summary is for** and what they will do with it.
- **Ask for quotes** for anything important, so you can check it.
- **Ask what is missing or uncertain.**
- **Watch length.** Very long inputs can lead to details in the middle being underweighted; split long material into sections and summarise each, then combine. See [context windows](../../explainers/concepts/context-windows.md).

**Long thread summary**
```
Summarise this email thread for [a director who has 2 minutes]: [paste].
What is being asked, what has been agreed, who is waiting on whom, and the
single decision needed from the reader. Quote the message that contains
each commitment.
```

## Failure modes

- **Misattribution.** The summary says "Sam agreed to deliver by Friday" when Sam said "maybe Friday if legal signs off". The quote requirement exposes this.
- **Invented action items.** Plausible tasks nobody agreed to. "Write 'not stated'" and "do not assign owners" reduce this.
- **Lost nuance.** Disagreements get smoothed into consensus. Ask explicitly for disagreements.
- **Transcript errors.** Names, numbers and product terms misheard. Many tools let you add a custom vocabulary.
- **Chilling effect.** Some people speak less candidly when recorded. Decide meeting by meeting.

## Common mistakes

- Recording external calls without telling the other side.
- Sending AI summaries without reading them.
- Letting every attendee run their own bot, so five vendors get the same audio.
- Keeping every recording forever by default.
- Treating the summary as the record when the transcript was wrong.

## Next steps

- Using summaries in a manager's week: [AI for managers](../playbooks/for-managers.md)
- Call notes in sales: [AI for sales](../playbooks/for-sales.md)
- Speech recognition behind it: [Whisper](../../papers/multimodal/49-whisper/summary.md)
- Why summaries can invent details: [hallucinations](../../learn/concepts/hallucinations.md), [Learning to Summarize from Human Feedback](../../papers/techniques/147-learning-to-summarize-from-human-feedback/summary.md)

## Sources

- Digital Media Law Project, *Recording Phone Calls and Conversations*: <https://www.dmlp.org/legal-guide/recording-phone-calls-and-conversations>
- Radford et al., *Robust Speech Recognition via Large-Scale Weak Supervision* (Whisper, 2022): <https://arxiv.org/abs/2212.04356>
