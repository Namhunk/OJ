import sys
from itertools import product

n, m = map(int, sys.stdin.readline().strip().split())
_list = list(i for i in range(1, n+1))

prod = list(product(_list, repeat= m))
for i in prod:
    print(*i)