import sys

nums = []
for _ in range(5):
    nums.append(int(sys.stdin.readline().strip()))

nums = sorted(nums)
print(sum(nums) // 5)
print(nums[2])