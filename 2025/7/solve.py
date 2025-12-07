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
        start = 0
        for k, v in self.mat.items():
            if v == "S":
                start = k
                break
        ic(start)
        down = 1 + 0j
        queue = [start]
        res = 0

        while len(queue):
            if all(p.real > self.n + 100 for p in queue):
                break
            cpy = queue.copy()
            queue = []
            for beam in cpy:
                ic(beam)
                np = beam + down
                if self.mat[np] == "^":
                    queue.append(np - 1j)
                    queue.append(np + 1j)
                    res += 1
                elif self.mat[np] == ".":
                    queue.append(np)
            queue = list(set(queue))
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
    # 13953 no
    # 13992 no
