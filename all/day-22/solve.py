#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 22
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def solve(self):
        for line in self.lines:
            lh, rh = line.split("~")
            x1, y1, z1 = [int(x) for x in lh.split(",")]
            x2, y2, z2 = [int(x) for x in rh.split(",")]
            # grows from 1 -> 2

            scale = [x2 - x1 + 1, y2 - y1 + 1, z2 - z1 + 1]
            u, v, w = scale

            print(
                f"SpawnCubeAtCoordinate({x1}, {z1}, {y1}, new Vector3({u}, {w}, {v}));"
            )


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
