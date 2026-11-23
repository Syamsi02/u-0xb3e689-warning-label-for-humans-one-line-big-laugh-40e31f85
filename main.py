"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings,
160 characters or fewer, to /output/entry.txt. The label is
132 characters: deadpan label wording, three recognisable
human habits, and the punch in the last few words.
"""

import os


LABEL = (
    "WARNING: Contents may talk to pets like co-workers, "
    "lose keys while holding them, and insist they are "
    "five minutes away for an hour."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LABEL.strip()
    assert 1 <= len(text) <= 160, "label must be 1-160 characters"
    assert "\n" not in text, "label must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
