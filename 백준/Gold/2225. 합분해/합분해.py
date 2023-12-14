import sys, math

n, k = map(int, sys.stdin.readline().strip().split())
print(math.comb(n+k-1, k-1)%(10**9))