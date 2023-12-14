import sys

nums = [0] * 10
N = sys.stdin.readline().strip()
for i in N:
    nums[int(i)] += 1

if nums[0] < 1: print(-1)
else:
    s = 0
    rs = ""
    for i in range(9, -1, -1):
        s += (i * nums[i])
        rs += (str(i)*nums[i])
    
    print(rs if s % 3 == 0 else -1)