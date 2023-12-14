import sys

N, K = map(int, sys.stdin.readline().strip().split())

x = 2
y = 1
z = 0
nums = []
while z < K:
    if y <= N//x and x * y not in nums:
        nums.append(x*y); y += 1; z += 1
    elif y <= N//x and x * y in nums:
        y += 1
    elif y > N//x:
        x += 1; y = 1
print(nums.pop())