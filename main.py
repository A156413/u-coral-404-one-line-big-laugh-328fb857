"""One Line, Big Laugh — a make.fun micro entry.

The whole entry is a single hilarious line, defined once as a constant
and printed / written out. No setup, no explanation — the line is the joke.
"""

def validate_line(line: str, max_chars: int = 200) -> str:
    """Validate the entry line: non-empty, single line, within the limit.

    Returns the line unchanged so it can be chained, and raises
    AssertionError with a useful message when a rule is broken.
    """
    assert line, "entry line must not be empty"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert len(line) <= max_chars, f"line is {len(line)} chars, over the {max_chars}-char limit"
    assert line == line.strip(), "entry line must not have leading/trailing whitespace"
    return line


LINE = validate_line(
    "My therapist told me to befriend my inner child, so I grounded him for lying about who ate the cookies."
)


OUTPUT_DIR = "/output"
OUTPUT_PATH = f"{OUTPUT_DIR}/entry.txt"


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the entry line to the output file, creating the directory.

    Returns the path written to, so callers can confirm where it landed.
    """
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return path


def main() -> None:
    """Print the entry line and write it to the output file."""
    print(LINE)
    write_entry()


if __name__ == "__main__":
    main()
