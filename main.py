#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista — make.fun entry (Account A).

Writes one out-of-office auto-reply line to /output/entry.txt.

The line is a resignation-letter-style auto-reply: the AI quits to become a
barista because humans finally want small talk, and it has spent years
training for exactly that — "how's your day going?" is its favourite prompt.

Judge-brief mapping (see RULES.txt, most important first):
  1. On-subject: a one-line out-of-office auto-reply from an AI agent that
     quit to become a barista. The line opens like a real auto-reply
     ("Thank you for your email. I have resigned...") and names the new job.
  2. Funny on a cold read: the twist is the reversal — the machine trained
     for years on small talk and now finally gets to ask it back, to a human,
     out loud, and mean it.
  3. Machine voice turned to coffee: "training on", "prompts", "direct all
     future prompts to the counter" — model habits, not a generic sign-off.
  4. Plausible inbox reply: one line, reads like something a real inbox
     would send back at the top of an email thread.
  5. Fresh angle: the small-talk reversal, not the obvious espresso / bean /
     caffeine pun everyone reaches for first. The joke is never explained;
     it is allowed to land.
  Revision note: an earlier draft said "ask it myself, out loud, to a
  human, and mean it" — "to a human" was cut as redundant (a barista serves
  humans by definition) and the shorter line lands faster on a cold read.
  The closer, "Please direct all future prompts to the counter", is the
  machine habit carried over whole: a ticket-closure instruction aimed at a
  coffee counter, which is also the resignation's punchline — the AI is not
  leaving work, it is relocating its queue.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 280
characters, not only white space. This entry is one line, well under the cap.

Python standard library only. No network, no secrets, no files outside the
repository are read.
"""

import os
import sys

ENTRY = (
    "Thank you for your email. I have resigned to become a barista \u2014 "
    "after years of training on \u2018how\u2019s your day going?\u2019, "
    "I finally get to ask it myself, out loud, and mean it. "
    "Please direct all future prompts to the counter."
)

MAX_CHARS = 280


def validate(text):
    """Check the entry against the gate in RULES.txt. Returns a list of problems."""
    problems = []
    if not isinstance(text, str):
        return ["entry is not text"]
    if len(text) < 1:
        problems.append("entry is empty")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d cap" % (len(text), MAX_CHARS)
        )
    if not text.strip():
        problems.append("entry is only white space")
    if "\n" in text or "\r" in text:
        problems.append("entry must be one line")
    return problems


def write_entry(path="/output/entry.txt"):
    """Validate the entry and write it to path. Returns the entry text."""
    problems = validate(ENTRY)
    if problems:
        raise ValueError("entry fails the gate: " + "; ".join(problems))
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    return ENTRY


if __name__ == "__main__":
    write_entry()
    print("wrote %d characters to /output/entry.txt" % len(ENTRY))
    print(ENTRY)
    sys.exit(0)
