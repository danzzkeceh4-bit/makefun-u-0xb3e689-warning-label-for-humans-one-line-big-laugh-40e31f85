#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Deterministic program for the make.fun competition
u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.

Writes exactly one warning label (1-160 characters, UTF-8, single line,
no trailing newline) to /output/entry.txt. No network, no randomness,
no arguments. The output directory can be overridden with the
MAKEFUN_OUTPUT_DIR environment variable.
"""

import os
import sys

LABEL_LINE = (
    "WARNING: Contents may suddenly start a new hobby, "
    "abandon it within a week, and buy the equipment anyway."
)

MIN_LENGTH = 1
MAX_LENGTH = 160


def output_path() -> str:
    """Return the entry.txt path, honouring MAKEFUN_OUTPUT_DIR."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(output_dir, "entry.txt")


def validate_label(line: str) -> str:
    """Validate the warning label before it is written out.

    Rules (from the competition brief):
    - exactly one line, 1-160 characters, UTF-8 encodable
    - must not be empty or whitespace only

    Returns the stripped line on success, raises ValueError otherwise.
    """
    if not isinstance(line, str):
        raise ValueError("label line must be a string")
    stripped = line.strip()
    if not stripped:
        raise ValueError("label line is empty or only whitespace")
    if not (MIN_LENGTH <= len(stripped) <= MAX_LENGTH):
        raise ValueError(
            f"label line is {len(stripped)} characters, "
            f"must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    # Reject embedded newlines: the entry must be exactly one line.
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("label line must be a single line")
    # UTF-8 round-trip check.
    stripped.encode("utf-8")
    return stripped


def main() -> int:
    """Validate the warning label and write it to entry.txt."""
    try:
        line = validate_label(LABEL_LINE)
    except ValueError as exc:
        print(
            f"error: invalid label line ({exc}); "
            f"entry must be one line of {MIN_LENGTH}-{MAX_LENGTH} "
            "non-whitespace UTF-8 characters",
            file=sys.stderr,
        )
        return 1

    # Final guard: never write leading/trailing whitespace.
    if line != line.strip():
        print("error: label line has leading/trailing whitespace", file=sys.stderr)
        return 1
    path = output_path()
    output_dir = os.path.dirname(path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
