import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().strip().split())
_list = list(i for i in range(1, n+1))

comre = list(combinations_with_replacement(_list, m))
for i in comre:
    print(*i)