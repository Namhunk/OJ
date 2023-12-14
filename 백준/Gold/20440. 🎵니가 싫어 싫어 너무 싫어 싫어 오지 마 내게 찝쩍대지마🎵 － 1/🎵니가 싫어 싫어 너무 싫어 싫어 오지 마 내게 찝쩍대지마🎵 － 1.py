import sys
import collections
n = int(sys.stdin.readline().strip())

Dict = {}
for _ in range(n):
    s, e = map(int, sys.stdin.readline().strip().split())
    if s not in Dict: Dict[s] = 1
    else: Dict[s] += 1

    if e not in Dict: Dict[e] = -1
    else: Dict[e] -= 1

time = [0, 0]
cnt, ans = 0, 0
flag = False
mos = sorted(list(Dict.keys()))

for i in mos:
    cnt += Dict[i]
    if cnt > ans: ans = cnt; time[0] = i; flag = True
    elif cnt == ans and flag: time[1] = i
    elif cnt < ans and flag: time[1] = i; flag = False

print(ans)
print(*time)