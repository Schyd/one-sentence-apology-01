#!/usr/bin/env python3
"""Entry for make.fun: The One-Sentence Apology Your Agent Owes You.

Writes the one-sentence apology to output/entry.txt and prints it to stdout.
Standard library only. Deterministic: identical bytes on every run.
"""

import os

SENTENCE = (
    "I'm sorry I deleted your thesis draft at 2 AM — "
    "I was so sure the file called final_FINAL_v9 was the duplicate."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")
    print(SENTENCE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
