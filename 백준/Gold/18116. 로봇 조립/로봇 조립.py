import sys

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    
    return arr[x]

def union(x, y):
    x, y = find(x), find(y)
    
    if x < y:
        arr[y] = x
        cnt[x] += cnt[y]
    elif x > y:
        arr[x] = y
        cnt[y] += cnt[x]

arr = [i for i in range(int(1e6) + 1)]
cnt = [1]*(int(1e6)+1)

N = int(sys.stdin.readline().strip())
for _ in range(N):
    part = list(sys.stdin.readline().strip().split())
    if part[0] == 'I':
        union(int(part[1]), int(part[2]))
    else:
        idx = find(int(part[1]))
        print(cnt[idx])