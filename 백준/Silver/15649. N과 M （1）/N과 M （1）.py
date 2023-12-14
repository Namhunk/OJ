import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().strip().split())
_list = list(i for i in range(1, n+1))

perm = list(permutations(_list, m))
for i in perm:
    print(*i)