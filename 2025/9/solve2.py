from math import ceil
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

        zipped = list(zip(pts, pts[1:]))
        zipped.append((pts[-1], pts[0]))

        adj = defaultdict(lambda: ".")

        greens = set()

        for u, v in zipped:
            if u[0] == v[0]:
                d = u[1] - v[1]
                for i in range(u[1], v[1] + 1) if d < 0 else range(v[1], u[1] + 1):
                    adj[complex(i, u[0])] = "G"
                    greens.add(complex(i, u[0]))
            elif u[1] == v[1]:
                d = u[0] - v[0]
                for i in range(u[0], v[0] + 1) if d < 0 else range(v[0], u[0] + 1):
                    adj[complex(u[1], i)] = "G"
                    greens.add(complex(u[1], i))
        for p in pts:
            adj[complex(p[1], p[0])] = "#"

        greens = list(greens)
        mp = complex(
            ceil(sum(g.real for g in greens) / len(greens)),
            ceil(sum(g.imag for g in greens) / len(greens)),
        )
        # ic| solve2.py:69 in solve()- 'SUCCESS at:', np: (2390+41848j)
        self.fill(2390 + 41848j, adj)

        # for i in range(20):
        #     for j in range(20):
        #         print(adj[complex(i, j)], end="")
        #     print()
        dists = []
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                p1, p2 = pts[i], pts[j]
                dx, dy = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
                if dx == 0 or dy == 0:
                    continue
                good = True
                for r in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    if not good:
                        break
                    for c in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                        if adj[complex(r, c)] not in "#G":
                            good = False
                            break
                if good:
                    dists.append((dx + 1, dy + 1))

        ic(dists)
        dists = sorted(dists, key=lambda v: v[0] * v[1])
        return dists[-1][0] * dists[-1][1]

    def fill(self, pos, adj):
        if adj[pos] != ".":
            return
        adj[pos] = "G"
        deltas = [-1 + 0j, 1 + 0j, -1j, 1j]
        for d in deltas:
            self.fill(pos + d, adj)


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
