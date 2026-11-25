"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message (at most 100 characters) for a bug fix
that made everything worse, to /output/entry.txt.

The output directory comes from MAKEFUN_OUTPUT_DIR when the harness
sets it, and falls back to /output. The line is a fixed literal written
by this program; nothing is read from the network, the environment
beyond the output path, or any other file.
"""

import os

LINE = "fix: stop users reporting bugs by removing the report button; bug reports down 100%"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
