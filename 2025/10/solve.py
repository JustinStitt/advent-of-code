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

    def bfs(self, goal, switches):
        Q = deque([("." * len(goal), 0, -1)])
        frequency = defaultdict(lambda: 0)

        while len(Q):
            state, presses, last_pressed_idx = Q.popleft()
            if state == goal:
                return presses
            useful_switches = self.get_most_useful_switches(
                switches, state, goal, frequency
            )
            for _, idx, new_state in useful_switches:
                if idx == last_pressed_idx:
                    continue
                switch = switches[idx]
                frequency[idx] += 1
                for idx, c in enumerate(state):
                    if idx in switch:
                        c = "#" if c == "." else "."
                Q.append(("".join(new_state), presses + 1, idx))
        return 0

    def get_most_useful_switches(self, switches, state, goal, frequency):
        all = []
        for idx, switch in enumerate(switches):
            new_state = []
            for cidx, c in enumerate(state):
                if cidx in switch:
                    c = "#" if c == "." else "."
                new_state.append(c)
            sames = sum(1 if goal[i] == new_state[i] else 0 for i in range(len(goal)))
            all.append((sames, idx, new_state))
        f = frequency
        all = sorted(all, reverse=True, key=lambda v: v[0] - (f[v[1]] ** 2) / 1e3)
        ic(all)
        return all

    def solve(self):
        res = 0
        for idx, line in enumerate(self.lines):
            print(f"handling line {idx+1} out of {len(self.lines)} lines", flush=True)
            sp = line.split()
            goal = sp[0][1:-1]
            switches = sp[1:]
            # joltages = switches[:-1]
            switches = [eval(x) for x in switches[:-1]]
            switches = [x if type(x) is tuple else (x, None) for x in switches]
            res += self.bfs(goal, switches)
            ic(line, goal, switches)
            ic(res)
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
"""
.##.
means we need to pick an odd number of swaps for 1 and 2 and an even number
for 0 and 3.
"""
