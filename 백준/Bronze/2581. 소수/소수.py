import sys

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

nums = []
for i in range(M, N + 1):
    k = 0
    for j in range(2, i):
        if i % j == 0:k = 1; break
    if k == 0 and i != 1: nums.append(i)

if len(nums) == 0: print(-1)
else:
    print(sum(nums))
    print(min(nums))