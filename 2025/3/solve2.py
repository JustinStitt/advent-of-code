import sys
import itertools
import functools
import re
import time
import pyperclip
from icecream import ic
from collections import defaultdict, Counter
from pathlib import Path


class Soln:
    def __init__(self, input_file: Path):
        with open(input_file, "r") as fd:
            self._raw = fd.read()
            self.lines = [line for line in self._raw.strip().split("\n")]
            self.mat = defaultdict(
                lambda: None,
                {
                    (r, c): char
                    for r, row in enumerate(self.lines)
                    for c, char in enumerate(row)
                },
            )
            self.n = len(self.lines)
            self.m = len(self.lines[0])

            ic(self.n, self.m)

    def solve(self):
        res = 0
        for line in self.lines:
            ic(line)
            paired = list(enumerate(line))
            s = sorted(paired, key=lambda v: v[1] + str(len(line) - v[0]), reverse=True)
            n = len(line)
            final = []
            pidx = -1
            for i in range(12, 0, -1):
                lim = n - i
                largest = [n, "/"]
                for i, p in enumerate(s):
                    if p[0] <= pidx:
                        continue
                    if p[0] > lim:
                        continue
                    if p[1] > largest[1]:
                        largest = [p[0], p[1]]
                pidx = largest[0]
                final.append(largest[1])
                ic(final, largest)

            ic(int("".join(final)))
            res += int("".join(final))
            ic(final)

        # 0123
        return res


# fmt: off
# Usage: $ python solve.py <input> {-d <disable icecream output>}
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    cwd = Path(__file__).parent.resolve()
    input_file = cwd / Path(sys.argv[1]).with_suffix('.in') if len(sys.argv) > 1 else cwd / Path("small.in")
    time_start = time.perf_counter()
    soln = Soln(input_file=input_file)
    ans = soln.solve()
    print(f"ans: <<{ans}>>")
    print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
    pyperclip.copy(str(ans))
# 173885423001879 high
# 173395380057437 low
