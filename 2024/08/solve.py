import sys
import itertools
import functools
import re
import time
from icecream import ic
from collections import defaultdict, Counter
from pathlib import Path

"""
..........
..........
..........
....a.....
..........
.....a....
..........
..........
..........
..........

idea:
create equation for the line between all pairs of same-frequency nodes

0. one node is A, other is B
1. get slope from A to B
2. place antinode at A with positive slope
3. place antinode with B at negative slope
"""


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
        frequencies = defaultdict(lambda: list())

        for r, line in enumerate(self.lines):
            for c, char in enumerate(line):
                if char not in ".#":
                    frequencies[char].append((r, c))

        antinodes = set()
        ic(frequencies)
        for k, v in frequencies.items():
            for a, b in itertools.combinations(v, 2):
                m = (b[0] - a[0], b[1] - a[1])
                antinode0 = (b[0] + m[0], b[1] + m[1])
                antinode1 = (a[0] - m[0], a[1] - m[1])
                if antinode0[0] in range(0, self.n) and antinode0[1] in range(
                    0, self.m
                ):
                    antinodes.add(antinode0)
                if antinode1[0] in range(0, self.n) and antinode1[1] in range(
                    0, self.m
                ):
                    antinodes.add(antinode1)
                ic(a, b, m, antinode0, antinode1)
        return len(antinodes)


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
