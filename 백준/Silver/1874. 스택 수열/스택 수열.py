import sys

n = int(sys.stdin.readline().strip())
num = [int(sys.stdin.readline().strip()) for _ in range(n)]
nums = []
stack = []
p = []
i = 1
k = 0
while len(stack) < n:
    if i <= num[k]:
        nums.append(i)
        p.append('+')
        i += 1
    else:
        if num[k] == nums[-1]:
            stack.append(nums.pop())
            p.append('-')
            k += 1
        else:
            p.clear()
            break
if len(p) == 0:print('NO')
else:
    for i in p:
        print(i)