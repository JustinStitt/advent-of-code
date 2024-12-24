from icecream import ic
from collections import defaultdict
import re

inp = [int(x) for x in input().strip()]
ic(inp)

finp = []
spaces = []
files = [num for i, num in enumerate(inp) if i % 2 == 0]
ic(files)

for i, num in enumerate(inp):
    if i % 2 == 0:
        _id = i // 2
        finp.append(str(num))
        # finp.extend([str(_id)] * num)
    else:
        finp.extend(["@"] * num)
print(finp)

s = "".join(finp)
ic(s)

str_to_id = defaultdict(lambda: None)
count = 0
for i, c in enumerate(finp):
    if c != "@":
        str_to_id[i] = count
        count += 1
ic(str_to_id)

in_brace = False
i = len(s) - 1
olen = len(s)
while i >= 0:
    if s[i] == "@" or in_brace:
        i -= 1
        continue
    if s[i] == ">":
        in_brace = True
        i -= 1
        continue
    if s[i] == "<":
        in_brace = False
        i -= 1
        continue
    num = int(s[i])
    s = s[:i] + s[i + 1 :]
    patt = f"@{{{num}}}"
    # cleaned = re.sub(r"<\d+>", "", s)
    # cleaned = re.sub(r"@+", "b", cleaned)
    ns, repc = re.subn(patt, "<" + "".join([str(str_to_id[i])] * num) + ">", s, count=1)
    if repc == 0:
        i -= 1
        continue
    s = ns
    len_diff = len(s) - olen
    ic(len_diff)

    ic(ns)
    ic(patt)
    i = len(s) - 1
    # ic(i)

"""
13
4
"""
