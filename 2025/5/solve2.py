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
        reading_nums = False
        nums = []
        ranges = []
        res = 0
        for line in self.lines:
            ic(line)
            if line == "":
                reading_nums = True
                continue
            if not reading_nums:
                l, r = line.split("-")
                ranges.append(range(int(l), int(r) + 1))
            if reading_nums:
                nums.append(int(line))

        # sort ranges by starting position
        s = sorted(ranges, key=lambda r: r.start)
        s.append(range(0, 0))  # to help with i+1 edgecase
        i = 0
        crange = s[i]
        new_ranges = []
        while True:
            ic(new_ranges)
            nrange = s[i + 1]
            ic(crange, nrange)
            if nrange == range(0, 0):
                new_ranges.append(crange)
                break
            if nrange.start <= crange.stop:
                if nrange.stop < crange.stop:
                    ic("no combine")
                    i += 1
                    # no combine
                    continue
                new_range = range(crange.start, nrange.stop)
                ic("combine to", new_range)
                crange = new_range
                i += 1
            else:
                new_ranges.append(crange)
                crange = nrange
                i += 1

        new_ranges = list(set(new_ranges))
        ic(s)
        ic(new_ranges)
        for r in new_ranges:
            res += r.stop - r.start
        ic(res)
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
# 496959342722963 high
# 351444905534776 high
