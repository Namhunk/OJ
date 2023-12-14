import sys, math

A, B, C = map(int, sys.stdin.readline().strip().split())

print(math.floor(A / (C-B) + 1) if B < C else -1)