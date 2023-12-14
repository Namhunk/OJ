import sys


nums = []
for _ in range(int(sys.stdin.readline().strip())):
    nums.append(int(sys.stdin.readline().strip()))
nums = sorted(nums)
for i in nums:
    print(i)