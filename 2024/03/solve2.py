import sys
import re
from icecream import ic

raw = sys.stdin.read()
repl = r"don't\(\).*?(?=do\(\))"
raw = re.sub(repl, "", raw, flags=re.DOTALL)
raw = re.sub(r"don't\(\).*$", "", raw, flags=re.DOTALL)

result = 0
patt = r"mul\((?P<m1>\d+),(?P<m2>\d+)\)"
for match in re.finditer(patt, raw):
    num1, num2 = (int(match["m1"]), int(match["m2"]))
    result += num1 * num2
print(result)
