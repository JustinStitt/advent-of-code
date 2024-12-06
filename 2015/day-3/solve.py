import sys

line = sys.stdin.readline().rstrip()

dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
santa = (0, 0)
robot = (0, 0)
seen = {santa}

for i in range(0, len(line) - 1, 2):
    santa_delta = dirs[line[i]]
    robot_delta = dirs[line[i + 1]]
    santa = tuple(x + y for (x, y) in zip(santa, santa_delta))
    robot = tuple(x + y for (x, y) in zip(robot, robot_delta))
    seen |= set([santa]) | set([robot])

print(f"Answer is: {len(seen)}")
