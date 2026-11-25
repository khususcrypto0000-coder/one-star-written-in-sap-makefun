"""One Star, Written in Sap.

Writes the one-star houseplant review to /output/entry.txt.
Standard library only.
"""

import os
import sys

ENTRY = (
    "One star. Every time a friend visits, he snips a cutting off me "
    "and calls it sharing the love. I'm down to three leaves and a stump, "
    "and he potted my arm yesterday, named it Hope, and waters it more "
    "than me."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    with open(OUTPUT_PATH, "rb") as f:
        read_back = f.read()
    assert read_back == data, "entry.txt is not byte-identical to ENTRY"
    assert not data.endswith(b"\n"), "entry.txt must have no trailing newline"
    text = read_back.decode("utf-8")
    assert 1 <= len(text) <= 279, "entry must be 1-279 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    print("wrote {} ({} chars)".format(OUTPUT_PATH, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
