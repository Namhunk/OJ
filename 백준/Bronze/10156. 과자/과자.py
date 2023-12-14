import sys
n, k, m = map(int,  sys.stdin.readline().strip().split())
print(n*k - m if n*k > m else 0)