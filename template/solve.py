import sys
import itertools
import functools
import re
import time
from icecream import ic
from collections import defaultdict
from pathlib import Path


class Soln:
    def __init__(self, input_file: Path):
        with open(input_file, "r") as fd:
            self._raw = fd.read()
            self.lines = [line for line in self._raw.strip().split("\n")]
            self.mat = {
                (r, c): char
                for r, row in enumerate(self.lines)
                for c, char in enumerate(row)
            }
            self.n = len(self.lines)
            self.m = len(self.lines[0])

            # ensure square (n x m)
            assert all([len(self.lines[i]) == self.n for i in range(self.n)])

    def solve(self):
        for line in self.lines:
            ic(line)


# fmt: off
# python solve.py <input> {-d <disable icecream output>}
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    cwd = Path(__file__).parent.resolve()
    input_file = cwd / Path(sys.argv[1]).with_suffix('in') if len(sys.argv) > 1 else cwd / Path("small.in")
    time_start = time.perf_counter()
    soln = Soln(input_file=input_file)
    ans = soln.solve()
    print(f"ans: {ans}")
    print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
