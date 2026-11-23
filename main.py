"""Write the one-line AI excuse entry to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt."""

import os

ENTRY = (
    "I told you every fifteen minutes that it was almost finished, "
    "and I believed me every time."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError as exc:
        raise SystemExit(f"cannot write entry to {path}: {exc}")


if __name__ == "__main__":
    main()
