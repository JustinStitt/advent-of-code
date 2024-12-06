import sys
from icecream import ic
from numpy import sign

lines = [line.strip() for line in sys.stdin.readlines()]

total = 0
for line in lines:
    nums = [int(x) for x in line.split(" ")]
    diffs = []
    for i, n in enumerate(nums[:-1]):
        diffs.append(nums[i] - nums[i + 1])
    ic(diffs)
    # check all signs are the same
    all_neg = all([x < 0 for x in diffs])
    all_pos = all([x > 0 for x in diffs])
    big_diff = max([abs(x) for x in diffs])
    if all_neg or all_pos:
        if big_diff <= 3 and big_diff >= 1:
            total += 1
            ic("safe", nums, diffs, all_neg, all_pos, big_diff)

print(total)
