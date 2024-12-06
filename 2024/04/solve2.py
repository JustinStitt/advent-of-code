import sys
import re
from icecream import ic

raw = sys.stdin.read()
# raw = raw.replace("\n", "")
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

n = len(raw[: raw.index("\n")]) + 1
ic(n)

"""
M.S
.A.
M.S
"""

total = 0

for i, c in enumerate(raw):
    try:
        if (
            c == "M"
            and raw[i + 2] == "S"
            and raw[i + n + 1] == "A"
            and raw[i + 2 * n] == "M"
            and raw[i + 2 * n + 2] == "S"
        ):
            total += 1
    except:
        ...
"""
S.S
.A.
M.M
"""

for i, c in enumerate(raw):
    try:
        if (
            c == "S"
            and raw[i + 2] == "S"
            and raw[i + n + 1] == "A"
            and raw[i + 2 * n] == "M"
            and raw[i + 2 * n + 2] == "M"
        ):
            total += 1
    except:
        ...
"""
S.M
.A.
S.M
"""

for i, c in enumerate(raw):
    try:
        if (
            c == "S"
            and raw[i + 2] == "M"
            and raw[i + n + 1] == "A"
            and raw[i + 2 * n] == "S"
            and raw[i + 2 * n + 2] == "M"
        ):
            total += 1
    except:
        ...
"""
M.M
.A.
S.S
"""

for i, c in enumerate(raw):
    try:
        if (
            c == "M"
            and raw[i + 2] == "M"
            and raw[i + n + 1] == "A"
            and raw[i + 2 * n] == "S"
            and raw[i + 2 * n + 2] == "S"
        ):
            total += 1
    except:
        ...
print(total)
