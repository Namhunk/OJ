import sys

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    
    return arr[x]

def union(x, y):
    x, y = find(x), find(y)
    check_trueth(x, y)
    if trueth[x]:
        cnt[x], cnt[y] = 0, 0
    
    if x < y:
        change_cnt(x, y)
        arr[y] = arr[x]
    elif x > y:
        change_cnt(y, x)
        arr[x] = arr[y]
    
    
def check_trueth(x, y):
    if trueth[x] != trueth[y]:
        trueth[x] = 1
        trueth[y] = 1

def change_cnt(x, y):
    if cnt[x] and cnt[y]:
        cnt[x] += cnt[y]
        cnt[y] = 0
    else:
        cnt[x] = max(cnt[x], cnt[y])
        cnt[y] = 0

n, m = map(int, sys.stdin.readline().strip().split())
arr = [i for i in range(n+1)]
trueth = [0] * (n+1)
cnt = [0] * (n+1)

know = list(map(int, sys.stdin.readline().strip().split()))
if know[0] >= 1:
    trueth[know[1]] = 1
    if know[0] > 1:
        for i in range(2, len(know)):
            union(know[i-1], know[i])

for _ in range(m):
    party = list(map(int, sys.stdin.readline().strip().split()))
    
    if party[0] > 1:
        for i in range(2, len(party)):
            union(party[i-1], party[i])
    
    chief = find(party[1])
    if not trueth[chief]: cnt[chief] += 1

print(sum(cnt))