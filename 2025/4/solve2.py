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
        res = 0
        deltas = [
            r + i
            for r, i in itertools.product([-1, 0, 1], [-1j, 0j, 1j])
            if r != 0 or i != 0
        ]

        while True:
            cpy = self.mat.copy()
            changed = False
            for p, v in cpy.items():
                if v == ".":
                    continue
                cnt = "".join([self.mat[p + delta] for delta in deltas]).count("@")
                if cnt < 4:
                    res += 1
                    changed = True
                    self.mat[p] = "."
            if not changed:
                break
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
