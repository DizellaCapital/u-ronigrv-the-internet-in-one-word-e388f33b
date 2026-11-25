"""Entry for make.fun bounty u-ronigrv-the-internet-in-one-word-e388f33b.

The word is "Captcha": the whole internet, in one word. Every human on
earth has been stopped by a little box and asked to prove, to a machine,
that they are not a machine. It is funny on its own — the robot
interrogating the human about being human — it is true of the internet as
a whole rather than any one site or app, it surprises (nobody's first
reach is a gatekeeper), and at seven bytes it lands in one beat, which
also helps the byte tie-break against longer words.
"""

import os
import sys

WORD = "Captcha"


def check_word(word):
    """The gate wants 1-30 UTF-8 characters, one word, not only whitespace."""
    if not word or word.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def run():
    """Validate the word, write it, then read it back to prove it landed."""
    check_word(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    with open(target, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if saved != WORD:
        raise SystemExit("read-back mismatch: entry.txt does not hold the word")


if __name__ == "__main__":
    try:
        run()
    except ValueError as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
