from icecream import ic

n = "812361289012"

paired = list(enumerate(n))
s = sorted(paired, key=lambda e: e[1], reverse=True)
ic(s)
