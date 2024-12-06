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
    if good:
        total += 1
        middle = nums[len(nums) // 2]
        ans += middle

print(total)
print(ans)
