import sys

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    
    return arr[x]

def union_or_war(k, x, y):
    x, y = find(x), find(y)
    
    if x != y:
        if  k == 1:
            if x < y:
                arr[y] = arr[x]
                cnt[x] += cnt[y]
            
            elif x > y:
                arr[x] = arr[y]
                cnt[y] += cnt[x]
        
        else:
            if cnt[x] < cnt[y]:
                arr[x] = arr[y]
                cnt[y] -= cnt[x]
                cnt[x] = 0
            
            elif cnt[x] > cnt[y]:
                arr[y] = arr[x]
                cnt[x] -= cnt[y]
                cnt[y] = 0
            
            else:
                cnt[x] = cnt[y] = 0

N, M = map(int, sys.stdin.readline().strip().split())
arr = [i for i in range(N+1)]
cnt = [0] * (N+1)

for i in range(1, N+1):
    cnt[i] = int(sys.stdin.readline().strip())

for _ in range(M):
    O, P, Q = map(int, sys.stdin.readline().strip().split())
    
    union_or_war(O, P, Q)

ans = []
for i in range(1, N+1):
    if arr[i] == i and cnt[i]:
        ans.append(cnt[i])

print(len(ans))
print(*sorted(ans))