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
                lambda: ".",
                {
                    complex(r, c): char
                    for r, row in enumerate(self.lines)
                    for c, char in enumerate(row)
                },
            )
            self.n = len(self.lines)
            self.m = len(self.lines[0])

            ic(self.n, self.m)

    def solve(self):
        pts = []
        for line in self.lines:
            x, y = [int(x) for x in line.split(",")]
            pts.append((x, y))
        dists = []
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                p1, p2 = pts[i], pts[j]
                dx, dy = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
                if dx == 0 or dy == 0:
                    continue
                dists.append((dx + 1, dy + 1))
        ic(dists)
        dists = sorted(dists, key=lambda v: v[0] * v[1])
        return dists[-1][0] * dists[-1][1]


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
