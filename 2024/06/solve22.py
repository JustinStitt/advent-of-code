import sys
from icecream import ic
from collections import defaultdict

lines = [x.strip() for x in sys.stdin.readlines()]

# seen = set()
curr = [0, 0]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] * 100000
dir = 0
n, m = len(lines), len(lines[0])
for r, line in enumerate(lines):
    ic(line)
    if "^" in line:
        curr[0] = r
        curr[1] = line.index("^")
        dir = 0
    elif ">" in line:
        curr[0] = r
        curr[1] = line.index(">")
        dir = 1
    elif "v" in line:
        curr[0] = r
        curr[1] = line.index("v")
        dir = 2
    elif "<" in line:
        curr[0] = r
        curr[1] = line.index("<")
        dir = 3


def get_vis(mat, curr, dir):
    seen = set()
    # seen = set()
    while (
        curr[0] >= 0 and curr[0] < len(mat) and curr[1] >= 0 and curr[1] < len(mat[0])
    ):
        seen.add(tuple(curr) + (dir % 4,))
        try:
            is_ob = mat[curr[0] + dirs[dir][0]][curr[1] + dirs[dir][1]] == "#"
            if is_ob:
                dir += 1
        except:
            ...
        curr[0] += dirs[dir][0]
        curr[1] += dirs[dir][1]
    return seen


def is_cycle(mat, curr, dir, new_wall):
    seen = defaultdict(lambda: set())
    skip = False
    while (
        curr[0] >= 0 and curr[0] < len(mat) and curr[1] >= 0 and curr[1] < len(mat[0])
    ):
        if not skip and (dir % 4) in seen[tuple(curr)]:
            return True
        if not skip:
            seen[tuple(curr)].add(dir % 4)
        try:
            is_ob = mat[curr[0] + dirs[dir][0]][curr[1] + dirs[dir][1]] == "#" or (
                curr[0] + dirs[dir][0] == new_wall[0]
                and curr[1] + dirs[dir][1] == new_wall[1]
            )
            if is_ob:
                dir += 1
                skip = True
            else:
                curr[0] += dirs[dir][0]
                curr[1] += dirs[dir][1]
                skip = False
        except:
            break

    return False


# cpy = lines[::]
# vis = get_vis(cpy, curr[:], dir)
counts = set()
# for vi in vis:
#     r, c, nd = vi
#     if r == curr[0] and c == curr[1]:
#         continue
#     # if lines[r][c] == "#":
#     #     continue
#     cpy = lines[::]
#     # ic(r, c, nd)
#     cpy[r] = cpy[r][:c] + "#" + cpy[r][c + 1 :]
#     if is_cycle(cpy, curr[:], dir):
#         counts.add((r, c))

print(len(counts))
mat = lines
for r in range(n):
    for c in range(m):
        if r == curr[0] and c == curr[1]:
            continue
        if lines[r][c] == "#":
            continue
        # cpy[r] = cpy[r][:c] + "#" + cpy[r][c + 1 :]
        if is_cycle(mat, curr[::], dir, [r, c]):
            counts.add((r, c))

print(len(counts))
#
# # print(len(seen))
# print(count)
# 1619 too high
# 1533 not right
