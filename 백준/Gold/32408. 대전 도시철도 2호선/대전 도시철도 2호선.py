import sys
input = sys.stdin.readline
"""
조건을 만족하는 두 교차로를 고르는 경우의 수를 출력

1호선은 1번 교차로와, N번 교차로를 잇는 경로
"""

import sys

input = sys.stdin.readline
# 재귀를 사용하지 않으므로 setrecursionlimit은 필요 없으나, 
# 만약의 경우를 위해 남겨두어도 무방합니다.

def solve():
    N = int(input().strip())
    nodes = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().strip().split())
        nodes[u].append(v)
        nodes[v].append(u)

    # 1. 반복문을 이용해 1호선 경로 찾기 (부모 노드 기록 방식)
    parent = [0] * (N + 1)
    stack = [1]
    parent[1] = -1 # 시작점 표시
    
    # 1번부터 시작해 모든 노드의 부모를 찾음 (트리 탐색)
    order = []
    while stack:
        curr = stack.pop()
        order.append(curr)
        for nx in nodes[curr]:
            if parent[nx] == 0:
                parent[nx] = curr
                stack.append(nx)

    # N번부터 거꾸로 올라가며 1호선(is_line1) 마킹
    is_line1 = [False] * (N + 1)
    curr = N
    while curr != -1:
        is_line1[curr] = True
        curr = parent[curr]

    # 2. 서브트리 크기 구하기 (반복문 방식)
    visit = [False] * (N + 1)
    for i in range(1, N + 1):
        if is_line1[i]:
            visit[i] = True

    sub_sizes = []
    for i in range(1, N + 1):
        if is_line1[i]:
            for start_node in nodes[i]:
                if not visit[start_node]:
                    # 여기서부터는 일반적인 DFS로 서브트리 크기 측정
                    size = 0
                    stack = [start_node]
                    visit[start_node] = True
                    while stack:
                        curr = stack.pop()
                        size += 1
                        for nx in nodes[curr]:
                            if not visit[nx]:
                                visit[nx] = True
                                stack.append(nx)
                    sub_sizes.append(size)

    # 3. 결과 계산
    total_not_line1 = sum(sub_sizes)
    ans = total_not_line1 * (total_not_line1 - 1) // 2
    for size in sub_sizes:
        ans -= size * (size - 1) // 2

    print(ans)

solve()
"""
1. 1호선은 1부터 N 지점까지의 연결을 1호선으로 할 수 있음
2. 이때 시작점, 끝점이 1, N으로 끝나지 않는 도로가 있다면 2호선을 만들 수 있음
---------------------------------------------
1. 1호선의 경로를 갖는 교차로를 찾는다
2. 1호선의 교차로를 사용해 다음 교차로에 방문한 적이 없는 경우 각 서브 트리의 크기를 구함
3. 각 서브 트리의 합을 구해 S, E 를 뽑는 전체 경우를 탐색, sum(K)C2 = ans
4. 각 서브 트리 안에서 경로가 생성되는 경우를 빼줌 for i in range(len(K)): ans -= K[i]C2

"""