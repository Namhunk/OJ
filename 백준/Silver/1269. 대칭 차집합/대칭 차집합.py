import sys

A, B = map(int, sys.stdin.readline().strip().split())
Ae = set(sys.stdin.readline().strip().split())
Be = set(sys.stdin.readline().strip().split())

print(len(Ae - Be) + len(Be - Ae))