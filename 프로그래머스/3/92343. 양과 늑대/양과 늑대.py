# 2 <= len(info) <= 17
def solution(info, edges):
    children = [[] for _ in range(len(info))]
    for p, c in edges:
        children[p].append(c)

    ans = 0

    def dfs(sheep, wolf, available):
        nonlocal ans
        ans = max(ans, sheep)

        for node in list(available):        # 현재 갈 수 있는 모든 노드 시도
            ns = sheep + (1 if info[node] == 0 else 0)
            nw = wolf  + (1 if info[node] == 1 else 0)

            if nw >= ns:                    # 늑대 >= 양이면 가지치기
                continue

            # 백트래킹: 다음 상태 만들고 재귀 → 자동으로 이전 상태 유지
            nxt = set(available)
            nxt.remove(node)
            for ch in children[node]:
                nxt.add(ch)

            dfs(ns, nw, nxt)

    dfs(1, 0, set(children[0]))             # 노드 0은 항상 양, 자식 집합으로 시작
    return ans

        
"""
모을 수 있는 양의 최대 마릿수
늑대는 현재 양의 마릿수보다 많으면 안됨
info: 각 노드가 양인지, 늑대인지
edges: 각 노드간의 연결 관계
edges[0]: 부모
edges[1]: 자식

동작 구상
0인 값부터 제거해야 하므로 heap
1. 모든 실행은 노드 0번 부터
2. 다음 노드가 늑대가 아닌 경우 이동 후 list에 자식 노드 저장
3. 2번에서 늑대만 남기 전까지 반복
4. 노드의 방문을 표시할 배열 visit
5. 배열에 늑대만 남은 경우 모든 위치들을 이동(양을 발견하기 전까지)
6. 양을 발견한 경우 해당 노드의 역순으로 거슬러가 visit[True]가 나오기 전까지 늑대를 더하고 거슬러 올라감

0

1   0

1   1

0   0
"""