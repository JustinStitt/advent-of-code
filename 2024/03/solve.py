import sys
import re
from icecream import ic

raw = sys.stdin.read()
patt = r"mul\((?P<m1>\d+),(?P<m2>\d+)\)"
result = 0
for match in re.finditer(patt, raw):
    num1, num2 = (int(match["m1"]), int(match["m2"]))
    result += num1 * num2
print(result)
