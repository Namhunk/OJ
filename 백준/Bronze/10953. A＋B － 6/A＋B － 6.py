import sys

for _ in range(int(sys.stdin.readline().strip())):
    a, b = map(int, sys.stdin.readline().strip().split(","))
    print(a+b)