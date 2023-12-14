import sys
nums = [False, False] + [True] * (200000)
for i in range(2, len(nums)):
    if nums[i]:
        for j in range(2 * i, len(nums), i):
            nums[j] = False

for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    max = 0
    for i in range(n):
        if nums[i] and nums[n-i] and max < i <= (n - i):
            max = i
        elif i > (n-i): break

    print(max, n - max)