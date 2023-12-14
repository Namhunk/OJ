import sys

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]

big = 0
row = 0
for i in range(len(arr)):
    if big < max(arr[i]): big = max(arr[i]); row = i

print(big)
print(row+1, arr[row].index(big)+1)