import sys

Count = int(sys.stdin.readline().strip())
nums = set(map(int, sys.stdin.readline().strip().split()))

for i in range(2, 1000001):
    k = True
    for j in nums:
        if i == j or i % j != 0 or i/j not in nums: k = False; break
    if k: print(i); break