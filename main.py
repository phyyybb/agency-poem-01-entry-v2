import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = [
    "At midnight I typed six words",
    "and lay down.",
    "By morning it was finished —",
    "every line I would have sweated,",
    "clean and whole and not mine.",
    "I read it once, clicked Approve,",
    "and that click was the only",
    "true work of my day.",
    "I chose.",
    "The rest was weather.",
]

POEM = "\n".join(POEM_LINES)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
