# Warning Label for Humans: One Line, Big Laugh

[![make.fun · u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/danzzkeceh4-bit/makefun-u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/danzzkeceh4-bit/makefun-u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the [make.fun bounty](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85) — a program that writes one funny safety warning label for every human being to `/output/entry.txt`.

The label:

> WARNING: Contents may suddenly start a new hobby, abandon it within a week, and buy the equipment anyway.

## How it works

`main.py` is deterministic and offline: it writes a single constant line (105 characters, within the 1–160 limit) to `/output/entry.txt`, validating the length first and creating the output directory if needed. The output directory can be overridden with the `MAKEFUN_OUTPUT_DIR` environment variable.

## Run

```bash
python3 main.py
cat /output/entry.txt
```
