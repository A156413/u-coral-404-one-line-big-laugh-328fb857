"""One Line, Big Laugh — a make.fun micro entry.

The whole entry is a single hilarious line, defined once as a constant
and printed / written out. No setup, no explanation — the line is the joke.
"""

LINE = "My therapist told me to befriend my inner child, so I grounded him for lying about who ate the cookies."

assert len(LINE) <= 200, f"line is {len(LINE)} chars, over the 200-char limit"


def main() -> None:
    print(LINE)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
