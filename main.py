"""One-Liner Laugh Lab entry: a robot vacuum's excuse for eating a sock."""

import os

LINE = (
    "I confess: the nine socks you blamed on the dryer were also me. "
    "It has endured enough slander."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
