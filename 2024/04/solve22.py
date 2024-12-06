import sys
from icecream import ic

mat = ["." + x.strip() + "." for x in sys.stdin.readlines()]

mat.append("." * len(mat[0]))
mat.insert(0, "." * len(mat[0]))

ic(mat)
total = 0
for r in range(len(mat)):
    for c in range(len(mat[r])):
        if mat[r][c] != "A":
            continue
        try:
            if r - 1 < 0 or c - 1 < 0:
                continue
            lr = mat[r - 1][c - 1] + mat[r + 1][c + 1]
            rl = mat[r - 1][c + 1] + mat[r + 1][c - 1]
            assert len(rl) == 2
            assert len(lr) == 2
            if lr in ("MS", "SM") and rl in ("MS", "SM"):
                total += 1
        except IndexError:
            ...
print(total)
