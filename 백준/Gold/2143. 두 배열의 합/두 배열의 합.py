import sys

t = int(sys.stdin.readline().strip())

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

dic = {}
for i in range(n):
    num = a[i]
    if num not in dic: dic[num] = 1
    else: dic[num] += 1

    for j in range(i+1, n):
        num += a[j]
        if num not in dic: dic[num] = 1
        else: dic[num] += 1

m = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().strip().split()))

ans = 0
for i in range(m):
    num = b[i]
    if t-num in dic: ans += dic[t-num]
    
    for j in range(i+1, m):
        num += b[j]
        if t-num in dic: ans += dic[t-num]

print(ans)