import sys
from collections import deque
input = sys.stdin.readline

# 그래프 이론, 그래프 탐색, 위상 정렬, 방향 비순환 그래프
# 첫째 줄에는 이들이 만나는 시간을, 둘째 줄에는 1분도 쉬지 않고 달려야 하는 도로의 수가 몇 개인지 출력
# 마지막에 도착하는 사람까지 도착하는 시간을 의미
# 가장 오래걸리는 시간, 가장 많은 도로 수를 출력?

# 첫째 줄에 도시의 개수 n(1 <= n <= 10,000)
n = int(input().strip())

# 둘째 줄에 도로의 개수 m(1 <= m <= 100,000)
m = int(input().strip())

graph = [[] for _ in range(n+1)] # 시작 - 도착
back = [[] for _ in range(n+1)] # 도착 - 시작
indegree = [0 for _ in range(n+1)]
time = [0]*(n+1) # 시간
visit = [0]*(n+1) # 방문
# m+2줄까지 도로의 출발 도시 번호, 도착 도시 번호, 걸리는 시간
for _ in range(m):
    s, e, t = map(int, input().strip().split())
    graph[s].append([e, t]) # 모든 도로는 일방통행
    back[e].append([s, t]) # 되돌아가는 경로
    indegree[e] += 1

# 지도를 그리는 사람들이 출발하는 도시, 도착 도시
start, end = map(int, input().strip().split())

que = deque([start])
while que: # 출발 - 도착 까지 가장 오래 걸리는 시간을 구함
    x = que.popleft()
    for next, t in graph[x]:
        indegree[next] -= 1
        time[next] = max(time[next], time[x]+t)
        if indegree[next] == 0:
            que.append(next)

cnt = 0
que.append(end)
visit[end] = 1
while que: # 도착지점에서 출발지점으로 돌아가며 쉬지않고 달려야 하는 도로를 구함
    x = que.popleft()
    for p, t in back[x]:
        if time[x] - time[p] == t:
            cnt += 1
            if visit[p] == 0:
                visit[p] = 1
                que.append(p)

print(time[end])
print(cnt)
"""
최대시간이 걸린 경로들의 도로 수
"""