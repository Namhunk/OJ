# 2 <= len(a) <= 300,000

import sys
sys.setrecursionlimit(10**6)

def solution(a, edges):
    n = len(a)

    # 전체 합이 0이 아니면 절대 모두 0으로 만들 수 없음
    if sum(a) != 0:
        return -1

    # 인접 리스트로 트리 구성
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    visited[0] = True

    answer = 0  # 연산 횟수 (64-bit 정수처럼 취급)

    def dfs(node):
        nonlocal answer

        # 자식들로 내려갔다가 올라오면서 값 모으기
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                child_val = dfs(nxt)   # 자식 서브트리의 최종 값
                answer += abs(child_val)
                a[node] += child_val   # 자식 값을 부모로 끌어올림

        # 이 노드의 최종 값 반환 (부모가 받아서 또 누적)
        return a[node]

    dfs(0)

    return answer

'''
모든 점들의 가중치를 0으로
연결된 두 점을 골라 각각 +1, -1 수행

모든 좌표를 1번씩만
'''