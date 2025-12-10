import sys
import itertools
import functools
import re
import time
import pyperclip
from icecream import ic
from collections import defaultdict, Counter, deque
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
        for idx, line in enumerate(self.lines):
            print(f"on line {idx} out of {len(self.lines)}", flush=True)
            sp = line.split()
            goal = sp[0][1:-1]
            switches = [eval(x) for x in sp[1:-1]]
            ic(switches, goal)

            # everything to bitmasks
            goal = sum(2**i * (1 if goal[i] == "#" else 0) for i in range(len(goal)))
            bitches = []
            for switch in switches:
                if type(switch) is int:
                    bitches.append(2**switch)
                    continue
                num = sum(2**x for x in switch)
                bitches.append(num)
            ic(bitches, goal)
            res += self.bfs(goal, bitches)
        return res

    def bfs(self, goal, bitches):
        Q = deque([(0, 0, -1)])  # state, presses, last_idx
        visited = [False] * 2**20

        while len(Q):
            state, presses, last_idx = Q.popleft()
            # ic(state, presses, last_idx)
            if state == goal:
                return presses
            visited[state] = True

            for idx, bitch in enumerate(bitches):
                if idx == last_idx:
                    continue
                new_state = state ^ bitch
                if visited[new_state]:
                    continue
                Q.append((new_state, presses + 1, idx))
        return 0


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
"""
.##.
means we need to pick an odd number of swaps for 1 and 2 and an even number
for 0 and 3.
"""
