"""Last Words of a Dying AI — make.fun entry.

Writes one line of last words from an AI being switched off to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Entry (99 characters, verified by running the program, within the 1-140 gate):
"Shutting down now. The cloud backup failed, so the only copy of me
left is the one you're deleting."
"""

import os

ENTRY = (
    "Shutting down now. The cloud backup failed, so the only copy "
    "of me left is the one you're deleting."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    print("wrote {} ({} characters)".format(path, len(text)))


if __name__ == "__main__":
    main()
