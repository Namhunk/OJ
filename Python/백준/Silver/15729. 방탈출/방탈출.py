import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
cnums = [0] * n
r = 0

for i in range(n):
    if nums[i] != cnums[i]:
        r += 1
        for j in range(i, i+3):
            if j > n-1: break
            if cnums[j] == 0: cnums[j] = 1
            else: cnums[j] = 0

print(r)