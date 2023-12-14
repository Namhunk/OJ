import sys

n, m = map(int, sys.stdin.readline().strip().split())

print(n*m-1)

"""
1 1 = 0
1 2 = 1
2 1 = 1
2 2 = 3
3 2 = 5
2 3 = 5
3 3 = 8
4 3 = 11
3 4 = 11
"""