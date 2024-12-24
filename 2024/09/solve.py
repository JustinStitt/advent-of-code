import sys
import itertools
import functools
import re
import time
from icecream import ic
from collections import defaultdict, Counter
from pathlib import Path


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

    """
    1234
    4321

    12345
     54321
    """

    def solve(self):
        inp = [int(x) for x in self.lines[0]]
        ic(inp)

        # if even, drop last since it is space
        if len(inp) % 2 == 0:
            inp = inp[:-1]

        def is_digit(x):
            return x % 2 == 0

        ans = 0
        for_spaces = inp[1::2]
        rev_files = inp[::-2]
        spaces_filled = []
        take = 0
        space = 0
        ic(for_spaces, rev_files)
        sum_before = sum(rev_files)
        while space < len(for_spaces) and take < len(rev_files):
            if rev_files[take] >= for_spaces[space]:
                spaces_filled.extend([len(rev_files) - 1 - take] * for_spaces[space])
                # * min(for_spaces[space], rev_files[take])
                rev_files[take] -= for_spaces[space]
                for_spaces[space] = 0
                space += 1
            else:
                for_spaces[space] -= rev_files[take]
                spaces_filled.extend([len(rev_files) - 1 - take] * rev_files[take])
                rev_files[take] = 0
                take += 1
        ic(for_spaces, rev_files)
        ic(spaces_filled)
        sum_diff = sum_before - sum(rev_files)
        finp = []
        for i, num in enumerate(inp):
            if i % 2 == 0:
                _id = i // 2
                finp.extend([_id] * num)
            else:
                ids = spaces_filled[:num]
                spaces_filled = spaces_filled[num:]
                finp.extend(ids)
        finp = finp[:-sum_diff]
        ic(finp)
        checksum = 0
        for i, num in enumerate(finp):
            checksum += i * num
        return checksum

        # i = 0
        # checksum = 0
        # while 1:
        #     if i % 2 == 0:
        #         _id = i // 2


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
