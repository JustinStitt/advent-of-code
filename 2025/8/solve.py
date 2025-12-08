import sys
import math
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
        pos = []
        for line in self.lines:
            s = line.split(",")
            x, y, z = [int(x) for x in s]
            ic(x, y, z)
            pos.append((x, y, z))

        dists = []

        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                u, v = pos[i], pos[j]
                d = math.dist(u, v)
                dists.append((u, v, d))

        dists = sorted(dists, key=lambda v: v[2])
        # take first 1000
        dists = dists[:1000]
        ic(dists, len(dists))

        adj_list = defaultdict(list)

        for u, v, d in dists:
            adj_list[u].append(v)
            adj_list[v].append(u)

        ic(adj_list)
        visited = set()

        gots = []
        for pos in adj_list.keys():
            got = self.dfs(pos, visited, adj_list)
            gots.append(got)
            ic(got)

        return functools.reduce(lambda x, y: x * y, sorted(gots, reverse=True)[:3])

    def dfs(self, pos, visited, adj) -> int:
        if pos in visited:
            return 0
        visited.add(pos)

        s = 1
        for neighbour in adj[pos]:
            s += self.dfs(neighbour, visited, adj)

        return s


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
