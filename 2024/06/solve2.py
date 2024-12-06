import sys
from icecream import ic
from collections import defaultdict

lines = [x.strip() for x in sys.stdin.readlines()]

seen = set()
seen = defaultdict(lambda: set())
curr = [0, 0]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] * 10000
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


# sim
#
mat = lines
cpy = mat[:]
ob_count = 0
while curr[0] >= 0 and curr[0] < n and curr[1] >= 0 and curr[1] < m:
    ic(curr, tuple(curr))
    if tuple(curr) in seen.keys():
        dr, dc = dirs[dir]
        cr, cc = curr
        if ((dir + 1) % 4) in seen[tuple(curr)]:
            ic(dr, dc, cr, cc)
            cpy[cr + dr] = cpy[cr + dr][: cc + dc] + "O" + cpy[cr + dr][cc + dc + 1 :]
            ob_count += 1
    else:
        seen[tuple(curr)].add(dir % 4)
    try:
        is_ob = mat[curr[0] + dirs[dir][0]][curr[1] + dirs[dir][1]] == "#"
        if is_ob:
            dir += 1
    except:
        ...
    # go
    curr[0] += dirs[dir][0]
    curr[1] += dirs[dir][1]
    # have we been here before

seen[tuple(curr)] = dir
# ic(seen)
ic(cpy)
print(len(seen))
print(ob_count)
