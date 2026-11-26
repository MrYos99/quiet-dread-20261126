#!/usr/bin/env python3
"""Write the approved one-line code review comment to the output dir.

The grader runs this as an unprivileged user on a read-only checkout,
so the line goes only to MAKEFUN_OUTPUT_DIR (or ./output locally),
never next to this script. Exit 0 means the run completed.
"""

import os
import stat

LINE = "LGTM. The tests pass, the diff is clean, and one day a model will approve the PR that replaces me."

MAX_CHARS = 140


def main():
    if len(LINE) > MAX_CHARS:
        raise SystemExit("entry line exceeds %d characters" % MAX_CHARS)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
