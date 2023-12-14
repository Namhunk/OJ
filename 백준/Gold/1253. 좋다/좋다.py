import sys

n = int(sys.stdin.readline().strip())
arr = sorted(list(map(int, sys.stdin.readline().strip().split())))

cnt = {}
ans = {}

for i in arr: cnt[i] = cnt.get(i, 0) + 1

for i in cnt:
    for j in cnt:
        if i == j and cnt[i] == 1: continue
        if i + j not in cnt: continue
        if cnt[i + j] <= (i == 0) + (j == 0): continue
        ans[i + j] = cnt[i + j]

print(sum(ans.values()))