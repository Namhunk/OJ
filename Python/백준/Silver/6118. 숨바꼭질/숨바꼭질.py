from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
dic = {}
distance = [float('inf')]*(n+1)
dic = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    dic[a].append(b)
    dic[b].append(a)

que = deque([1])
distance[1] = 0
while que:
    x = que.popleft()
    for i in dic[x]:
        if distance[i] > distance[x]+1:
            distance[i] = distance[x]+1
            que.append(i)

print(distance.index(max(distance[1: n+1])), max(distance[1: n+1]), distance.count(max(distance[1: n+1])))