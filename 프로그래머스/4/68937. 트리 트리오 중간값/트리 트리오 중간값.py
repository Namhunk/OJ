from collections import defaultdict

def dfs(start, n, graph):
    stack = [(start, 0)]
    visited = [False] * (n + 1)
    visited[start] = True

    max_node = start
    max_dist = 0
    unique = 1  # 최대 거리 정점이 유일하면 1, 여러 개면 0

    while stack:
        node, dist = stack.pop()

        if dist > max_dist:
            max_node = node
            max_dist = dist
            unique = 1
        elif dist == max_dist:
            unique = 0

        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, dist + 1))

    return max_node, max_dist, unique


def solution(n, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    start, _, _ = dfs(1, n, graph)
    end, diameter, unique = dfs(start, n, graph)
    print(diameter)

    if unique == 0:
        return diameter

    _, diameter, unique = dfs(end, n, graph)
    print(diameter)
    return diameter if unique == 0 else diameter - 1