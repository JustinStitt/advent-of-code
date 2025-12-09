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
            self.adj = None

            ic(self.n, self.m)

    def solve(self):
        pts = []
        ptscpy = []
        for line in self.lines:
            x, y = [int(x) for x in line.split(",")]
            pts.append(complex(y, x))
            ptscpy.append((x, y))

        zipped = list(zip(pts, pts[1:]))
        zippedcpy = list(zip(ptscpy, ptscpy[1:]))
        zipped.append((pts[-1], pts[0]))
        zippedcpy.append((ptscpy[-1], ptscpy[0]))
        pos = set()
        for u, v in zipped:
            if u.real == v.real:
                for c in (
                    range(int(u.imag), int(v.imag) + 1)
                    if u.imag < v.imag
                    else range(int(v.imag), int(u.imag) + 1)
                ):
                    pos.add(complex(u.real, c))
            elif u.imag == v.imag:
                for r in (
                    range(int(u.real), int(v.real) + 1)
                    if u.real < v.real
                    else range(int(v.real), int(u.real) + 1)
                ):
                    pos.add(complex(r, u.imag))
        adj = defaultdict(lambda: ".")

        greens = set()
        for u, v in zippedcpy:
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
        for p in ptscpy:
            adj[complex(p[1], p[0])] = "#"

        for i in range(20):
            for j in range(20):
                print(adj[complex(i, j)], end="")
            print()

        valid = []
        self.adj = adj
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                a, b = pts[i], pts[j]
                rd = a.real - b.real
                cd = a.imag - b.imag
                if rd == 0 or cd == 0:
                    continue
                c1 = complex(a.real, b.imag)
                c2 = complex(b.real, a.imag)
                ic(c1, c2)
                # ic| solve3.py:65 in solve()- c1: (1+7j), c2: (3+11j)
                # c1g = any(c1.real in r for r in pairon_r[c1.imag]) and any(
                #     c1.imag in r for r in pairon_c[c1.real]
                # )
                # c2g = any(c2.real in r for r in pairon_r[c2.imag]) and any(
                #     c2.imag in r for r in pairon_c[c2.real]
                # )
                if not self.escape(c1) and not self.escape(c2):
                    ic("wow", a, b)
                # if c1 in pos and c2 in pos:
                #     # 3,7 1,11
                #     dx = abs(a.imag - b.imag)
                #     dy = abs(a.real - b.real)
                #     valid.append(dx * dy)
                #     # valid.append(abs(a.real - b.real) * abs(a.imag - b.imag))
                #     ic("wow", a, b)
        ic(valid)

    @functools.lru_cache()
    def escape(self, pos):
        if self.adj[pos] in "G#":
            return False
        if pos.real < 0 or pos.real > 100_000 or pos.imag < 0 or pos.imag > 100_000:
            return True
        deltas = [-1 + 0j, 1 + 0j, -1j, 1j]
        return all(self.escape(pos + d) for d in deltas)

        # ic(a, b, c1, c2)


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
