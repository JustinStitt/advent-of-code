import sys
from icecream import ic
from numpy import sign

lines = [line.strip() for line in sys.stdin.readlines()]

total = 0


def safe(nums):
    diffs = []
    for i, n in enumerate(nums[:-1]):
        diffs.append(nums[i] - nums[i + 1])
    # check all signs are the same
    all_neg = all([x < 0 for x in diffs])
    all_pos = all([x > 0 for x in diffs])
    big_diff = max([abs(x) for x in diffs])
    if all_neg or all_pos:
        if big_diff <= 3 and big_diff >= 1:
            return True
    return False


total = 0
for line in lines:
    nums = [int(x) for x in line.split(" ")]
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i + 1 :]
        if safe(new_nums):
            total += 1
            break

print(total)
