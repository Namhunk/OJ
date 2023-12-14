import sys

Count = [0] * 2 * (10**7)

N = int(sys.stdin.readline().strip())
NList = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
MList = list(map(int, sys.stdin.readline().strip().split()))

for i in NList:
    Count[10**7 + i] += 1

for i in MList:
    print(1 if Count[10**7+i] != 0 else 0, end=" ")