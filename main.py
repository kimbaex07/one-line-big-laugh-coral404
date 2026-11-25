"""One Line, Big Laugh — make.fun entry for @kim-bae.

Writes a single original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is the whole entry: no title, setup or explanation around it.
"""

import os

LINE = "My dentist told me to floss the teeth I want to keep, so I flossed one tooth and named him Gregory."


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
