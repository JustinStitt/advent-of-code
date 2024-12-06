import sys
from icecream import ic
from collections import defaultdict


# -1, 0  0, 1  1, 0  0, -1
# 0, 1   1, 0  0, -1
def next_dir(dir):
    return dir[1], -dir[0]


def go(mat, pos, dir=(-1, 0)):
    seen = defaultdict(lambda: set())
    while mat.get(pos, None):
        r, c = pos
        dr, dc = dir
        dest = mat.get((r + dr, c + dc), None)
        if dest == "#":
            dir = next_dir(dir)
            continue
        if dir in seen[(r, c)]:
            return "cycle"
        seen[(r, c)].add(dir)
        pos = (r + dr, c + dc)

    return seen


def get_start(mat, find="^"):
    for pos, char in mat.items():
        if char == find:
            return pos
    return None


def main():
    inp = sys.stdin.read()

    mat = {
        (r, c): char
        for r, row in enumerate(inp.strip().split("\n"))
        for c, char in enumerate(row)
    }

    start = get_start(mat)
    ic(start)

    visited = go(mat, start)
    count = 0
    for v in visited.keys():
        r, c = v
        if mat[r, c] != ".":
            continue
        mat[r, c] = "#"
        resp = go(mat, start)
        mat[r, c] = "."
        if resp == "cycle":
            count += 1
    print(count)


main()
