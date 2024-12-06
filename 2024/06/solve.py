import sys
from icecream import ic

lines = [x.strip() for x in sys.stdin.readlines()]

seen = set()
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


ic(curr)

# sim
#
mat = lines
while curr[0] >= 0 and curr[0] < n and curr[1] >= 0 and curr[1] < m:
    try:
        is_ob = mat[curr[0] + dirs[dir][0]][curr[1] + dirs[dir][1]] == "#"
        if is_ob:
            dir += 1
    except:
        ...
    # go
    mat[curr[0]] = mat[curr[0]][: curr[1]] + "X" + mat[curr[0]][curr[1] + 1 :]
    curr[0] += dirs[dir][0]
    curr[1] += dirs[dir][1]
    seen.add(tuple(curr))

print(len(seen))
