import sys
import re
from icecream import ic
from collections import defaultdict

lines = [line.strip() for line in sys.stdin.readlines()]

befores = defaultdict(lambda: list())

rest = []

for i, line in enumerate(lines):
    if line == "":
        rest = lines[i + 1 :]
        break
    a, b = [int(x) for x in line.split("|")]
    befores[b].append(a)

ic(rest, befores)
total = 0
ans = 0
incorrect = []
for line in rest:
    nums = [int(x) for x in line.split(",")]
    ic(nums)
    good = True
    for idx, num in enumerate(nums):
        for b in befores[num]:
            try:
                if nums.index(b) > idx:
                    good = False
                    break
            except ValueError:
                ...
    if not good:
        incorrect.append(nums[:])

ic(incorrect)


class Val:
    def __init__(self, val):
        self.val = val

    def __gt__(self, other):  # can also define lt
        return other.val in befores[self.val]

    def __repr__(self):
        return str(self.val)


ans = 0
for inc in incorrect:
    inc2 = [Val(x) for x in inc]
    ic("unsorted: ", inc2)
    inc2 = sorted(inc2)
    ic("sorted: ", inc2)
    middle = inc2[len(inc2) // 2]
    ans += middle.val
print(ans)
