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
            )
            self.n = len(self.lines)
            self.m = len(self.lines[0])

            ic(self.n, self.m)

    def solve(self):
        res = 0
        row = 0
        col = 0
        mc = 0
        ic(self._raw)
        for _, ch in enumerate(self._raw):
            if ch == "\n":
                ic("new line")
                row += 1
                mc = max(mc, col)
                col = 0
                continue
            p = complex(row, col)
            self.mat[p] = ch
            col += 1
        ic(self.mat, row, mc)
        op = None
        numbers = []
        res = 0
        for c in range(mc):
            num = []
            for r in range(row):
                sym = self.mat[complex(r, c)]
                ic(sym)
                if sym in "*+":
                    if op == "*":
                        res += functools.reduce(lambda u, v: u * v, numbers)
                    elif op == "+":
                        res += functools.reduce(lambda u, v: u + v, numbers)
                    if op is not None:
                        numbers = []
                    op = sym
                if sym in "0123456789":
                    num.append(sym)
                if len(num) and r == row - 1:
                    val = int("".join(num).strip())
                    numbers.append(val)
        if op == "*":
            res += functools.reduce(lambda u, v: u * v, numbers)
        elif op == "+":
            res += functools.reduce(lambda u, v: u + v, numbers)
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
    # no 4945659218748
