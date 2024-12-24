from icecream import ic
from dataclasses import dataclass
import itertools

ic.disable()


@dataclass
class Spot:
    id: int | None
    count: int
    is_space: bool

    def __iter__(self):
        yield from [self.id] * self.count

    def __repr__(self):
        return str(list(self))

    @staticmethod
    def solve(spots: list["Spot"]):
        print("solving", flush=True)
        lst = list(itertools.chain.from_iterable([list(x) for x in spots]))
        i = 0
        checksum = 0
        ic(lst)
        while i < len(lst):
            if lst[i] is not None:
                checksum += lst[i] * i
            i += 1
        return checksum


inp = [int(x) for x in input().strip()]
ic(inp)

spots = []

for i, num in enumerate(inp):
    if i % 2 == 0:
        spots.append(Spot(id=i // 2, count=num, is_space=False))
    else:
        spots.append(Spot(id=None, count=num, is_space=True))

i = len(spots) - 1
while i >= 0:
    spot = spots[i]
    if spot.is_space:
        i -= 1
        continue
    found = None
    for j, espot in enumerate(spots):
        if not espot.is_space:
            continue
        if espot.count >= spot.count:
            found = j
            break

    if found is not None and found < i:
        spots[found].count -= spot.count
        spots = (
            spots[:found]
            + [spot]
            + spots[found:i]
            + [Spot(id=None, count=spot.count, is_space=True)]
            + spots[i + 1 :]
        )
        continue

    i -= 1
ic(spots)
print(Spot.solve(spots))
