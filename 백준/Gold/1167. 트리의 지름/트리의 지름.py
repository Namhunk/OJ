import sys
input = sys.stdin.readline

from collections import deque
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다.
# 트리의 지름을 구하는 프로그램을 작성

# 트리의 정점의 개수 V (2 <= V <= 100,000)
V = int(input().strip())
tree = [[] for _ in range(V+1)]
# 정점 번호는 1부터 V까지 존재
# V개의 줄에 걸쳐 간선의 정보
for _ in range(V):
    row = list(map(int, input().strip().split()))
    for i in range(1, len(row)-1, 2):
        tree[row[0]].append((row[i], row[i+1]))

def BFS(start, end = 0): # 시작 위치, 종점
    que = deque()
    que.append((start, 0))

    visited = [0]*(V+1)

    res = 0
    maxNode = 0

    while que:
        node, dist = que.popleft()
        visited[node] = 1 # 정점 방문 표시

        if end and node == end: # 종점이 정해졌다면
            return dist # 거리 반환

        for next_node in tree[node]:
            if visited[next_node[0]]: # 방문 하지 않은 정점들 만
                continue

            if res < dist+next_node[1]:
                res = dist + next_node[1]
                maxNode = next_node[0]

            que.append((next_node[0], dist+next_node[1]))

    return maxNode

start = BFS(1)
end = BFS(start)

print(BFS(start, end))