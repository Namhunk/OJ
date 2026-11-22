import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().strip().split())
_list = list(i for i in range(1, n+1))

combi = list(combinations(_list, m))
for i in combi:
    print(*i)