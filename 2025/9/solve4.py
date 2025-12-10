import sys
import itertools
import functools
import re
import time
import pyperclip
from icecream import ic
from collections import defaultdict, Counter
from pathlib import Path

NORTH, EAST, SOUTH, WEST = (0, 1, 2, 3)
sys.setrecursionlimit(2_140_000_000)


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
            self.adj = defaultdict(lambda: ".")
            self.n = len(self.lines)
            self.m = len(self.lines[0])
            self.edges = []

            ic(self.n, self.m)

    def get_dir(self, a, b):
        if a.real == b.real:
            d = a.imag - b.imag
            if d > 0:  # west
                return WEST
            elif d < 0:  # east
                return EAST
        elif a.imag == b.imag:
            d = a.real - b.real
            if d > 0:  # north
                return NORTH
            elif d < 0:  # south
                return SOUTH
        return NORTH

    def solve(self):
        pts = []
        for line in self.lines:
            x, y = [int(x) for x in line.split(",")]
            pts.append(complex(y, x))

        zipped = list(zip(pts, pts[1:]))
        zipped.append((pts[-1], pts[0]))
        ic(zipped)

        for u, v in zipped:
            if u.imag == v.imag:
                d = u.real - v.real
                for i in (
                    range(int(u.real), int(v.real) + 1)
                    if d < 0
                    else range(int(v.real), int(u.real) + 1)
                ):
                    self.adj[complex(i, u.imag)] = "G"
            elif u.real == v.real:
                d = u.imag - v.imag
                for i in (
                    range(int(u.imag), int(v.imag + 1))
                    if d < 0
                    else range(int(v.imag), int(u.imag) + 1)
                ):
                    self.adj[complex(u.real, i)] = "G"
        pdir = None
        cdir = None
        for i, (a, b) in enumerate(zipped):
            if pdir is None:
                pdir = self.get_dir(a, b)
                continue
            cdir = self.get_dir(a, b)
            self.adj[a] = "#"
            self.adj[b] = "#"
            if pdir == cdir:
                ic("here", pdir, cdir, a, b)
                self.adj[a] = "G"
            pdir = cdir

        dists = []
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                a, b = pts[i], pts[j]
                area = int(abs(a.real - b.real) + 1) * int(abs(a.imag - b.imag) + 1)
                dist = abs(a.real - b.real) + abs(a.imag - b.imag)
                dists.append((a, b, area))

        dists = sorted(dists, key=lambda v: v[2], reverse=True)
        valid = []
        self.edges = zipped
        # self.adj[5 + 5j] = "B"
        # ic(self.new_new_new_inside(5 + 5j))

        for i in range(20):
            for j in range(20):
                print(self.adj[complex(i, j)], end="")
            print()
        # exit(1)

        for a, b, d in dists:
            # if a != 7 + 11j or b != 3 + 2j:
            #     continue
            ic(a, b, d)
            tl = complex(min(a.real, b.real), min(a.imag, b.imag))
            tr = complex(min(a.real, b.real), max(a.imag, b.imag))
            bl = complex(max(a.real, b.real), min(a.imag, b.imag))
            br = complex(max(a.real, b.real), max(a.imag, b.imag))
            inside = complex(tl.real + 1, tl.imag + 1)
            if self.is_segment_intersected(tl, tr):
                continue
            if self.is_segment_intersected(tr, br):
                continue
            if self.is_segment_intersected(br, bl):
                continue
            if self.is_segment_intersected(bl, tr):
                continue
            res = self.new_new_new_inside(inside)
            if res % 2 == 1:
                ic("got valid: ", a, b, d)
                # valid.append(d)
                return d

        ic(valid)
        return max(valid)

    @functools.lru_cache()
    def is_segment_intersected(self, a, b):
        all_pts = []
        direction = self.get_dir(a, b)
        if direction == NORTH:
            for r in range(int(b.real), int(a.real) + 1):
                all_pts.append(complex(r, a.imag))
        elif direction == SOUTH:
            for r in range(int(a.real), int(b.real) + 1):
                all_pts.append(complex(r, a.imag))
        elif direction == EAST:
            for c in range(int(a.imag), int(b.imag) + 1):
                all_pts.append(complex(a.real, c))
        elif direction == WEST:
            for c in range(int(b.imag), int(a.imag) + 1):
                all_pts.append(complex(a.real, c))

        for p in all_pts:
            if self.adj[p] == ".":
                res = self.new_new_new_inside(p)
                return not res
        return False

    @functools.lru_cache()
    def new_new_new_inside(self, pt):
        hits = 0
        intersections = set()

        for a, b in self.edges:
            # calculate intersection point from east-ward line from pt to edge
            direction = self.get_dir(a, b)
            if direction in (EAST, WEST):
                if pt.real == a.real and pt.imag < a.imag:
                    intersection = complex(pt.real, a.imag)
                    if intersection in intersections:
                        continue
                    intersections.add(intersection)
                    intersections.add(complex(pt.real, b.imag))
                    hits += 1
                continue
            minr = int(min(a.real, b.real))
            maxr = int(max(a.real, b.real))
            if a.imag > pt.imag and pt.real in range(minr + 1, maxr):
                intersection = complex(pt.real, a.imag)
                if intersection in intersections:
                    continue
                ic("c", a, b)
                hits += 1
        ic(pt, hits)
        return hits

    @functools.lru_cache()
    def new_new_inside(self, pt):
        lim = 15_000
        if pt.real < 0 or pt.real > lim or pt.imag < 0 or pt.imag > lim:
            return 0
        if self.adj.get(pt) == "#":
            return 0
        s = 0
        if self.adj.get(pt) == "G":
            s = 1
        s += self.new_new_inside(pt - 1)
        return s

    def inside(self, pt, cache):
        return all(
            self.new_inside(pt, dir, cache) for dir in [NORTH, EAST, SOUTH, WEST]
        )

    def new_inside(self, pt, dir, cache):
        if cache.get(pt) is not None:
            return cache.get(pt)
        lim = 100_000
        if pt.real < 0 or pt.real > lim or pt.imag < 0 or pt.imag > lim:
            return False
        i = 0
        if self.adj[pt] in "G#":
            i = 1
        if dir == NORTH:
            i += self.new_inside(pt - 1, dir, cache)
        elif dir == EAST:
            i += self.new_inside(pt + 1j, dir, cache)
        elif dir == SOUTH:
            i += self.new_inside(pt + 1, dir, cache)
        elif dir == WEST:
            i += self.new_inside(pt - 1j, dir, cache)
        return i % 2 == 1


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
    # 4748688420 high
    # 4638152834 high
    # 4731260968
