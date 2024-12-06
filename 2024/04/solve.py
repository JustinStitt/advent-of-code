import sys
import re
from icecream import ic

raw = sys.stdin.read()
ic(raw)
"""
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""

xmaslr = raw.count("XMAS")
xmasrl = raw.count("SAMX")

n = len(raw[: raw.index("\n")]) + 1
ic(n)

total = xmaslr + xmasrl
# check col xmas
for i, c in enumerate(raw):
    if c == "\n":
        continue
    try:
        if (
            c == "X"
            and raw[i + n] == "M"
            and raw[i + 2 * n] == "A"
            and raw[i + 3 * n] == "S"
        ):
            total += 1
    except:
        ...

# check col xmas
for i, c in enumerate(raw):
    if c == "\n":
        continue
    try:
        if (
            c == "S"
            and raw[i + n] == "A"
            and raw[i + 2 * n] == "M"
            and raw[i + 3 * n] == "X"
        ):
            total += 1
    except:
        ...

# check diag
# check col xmas
n = n - 1  # 10
for i, c in enumerate(raw):
    if c == "\n":
        continue
    try:
        if (
            c == "X"
            and raw[i + n] == "M"
            and raw[i + 2 * n] == "A"
            and raw[i + 3 * n] == "S"
        ):
            ic("xmas diag 1")
            total += 1
    except:
        ...
for i, c in enumerate(raw):
    if c == "\n":
        continue
    try:
        if (
            c == "S"
            and raw[i + n] == "A"
            and raw[i + 2 * n] == "M"
            and raw[i + 3 * n] == "X"
        ):
            ic("xmas diag 1")
            total += 1
    except:
        ...

n = n + 2  # 12
for i, c in enumerate(raw):
    if c == "\n":
        continue
    try:
        if (
            c == "S"
            and raw[i + n] == "A"
            and raw[i + 2 * n] == "M"
            and raw[i + 3 * n] == "X"
        ):
            ic("samx diag 2")
            total += 1
    except:
        ...
for i, c in enumerate(raw):
    if c == "\n":
        continue
    try:
        if (
            c == "X"
            and raw[i + n] == "M"
            and raw[i + 2 * n] == "A"
            and raw[i + 3 * n] == "S"
        ):
            ic("samx diag 2")
            total += 1
    except:
        ...

print(total)
