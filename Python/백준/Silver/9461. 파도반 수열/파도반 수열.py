import sys

def padoban(nums, i):
    nums.append(nums[i-3]+nums[i-2])
    return nums

for _ in range(int(sys.stdin.readline().strip())):
    nums = [0, 1, 1, 1]

    n = int(sys.stdin.readline().strip())
    if n <= 3: nums[n]
    else:
        for i in range(4, n+1):
            padoban(nums, i)
    
    print(nums[-1])