from collections import deque

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    before = [0] * n   # before[b] = a : b를 방문하려면 a 먼저
    after = [-1] * n   # after[a] = b : a를 방문하면 b 해제
    for a, b in order:
        if b == 0:
            return False
        before[b] = a
        after[a] = b

    visited = [False] * n
    waiting = [False] * n
    q = deque([0])
    visited[0] = True

    while q:
        x = q.popleft()

        # x를 방문했을 때 열리는 방
        if after[x] != -1:
            y = after[x]
            before[y] = 0
            if waiting[y] and not visited[y]:
                visited[y] = True
                q.append(y)

        for nx in graph[x]:
            if visited[nx]:
                continue

            if before[nx] != 0:
                waiting[nx] = True
                continue

            visited[nx] = True
            q.append(nx)

    return all(visited)