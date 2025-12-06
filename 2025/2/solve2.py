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

    def only_dupes(self, n: int) -> bool:
        s = str(n)
        l = len(s)
        for i in range(1, l // 2 + 1):
            segments = []
            for sp in range(0, l, i):
                segments.append(s[sp : sp + i])
            if len(set(segments)) == 1:
                return True

        return False

    def solve(self):
        res = 0
        for line in self.lines:
            vals = line.split(",")
            ranges = []
            for val in vals:
                s = val.split("-")
                ranges.append([int(s[0]), int(s[1])])
            ic(ranges)
            for r in ranges:
                for n in range(r[0], r[1] + 1):
                    s = str(n)
                    if self.only_dupes(n):
                        res += n
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
