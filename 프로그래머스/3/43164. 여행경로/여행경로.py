def solution(tickets):
    # 출발지별 도착지 리스트 + 방문 여부 배열 생성
    FT = {}
    visit = {}
    for a, b in tickets:
        if a not in FT:
            FT[a] = []
            visit[a] = []
        FT[a].append(b)
        visit[a].append(False)

    # 알파벳 순으로 가장 앞선 경로를 만들기 위해 도착지 정렬
    for k in FT:
        # 도착지를 정렬하면서 visit 배열도 같은 순서를 유지해야 함
        # zip으로 묶어서 같이 정렬
        tmp = list(zip(FT[k], visit[k]))
        tmp.sort(key=lambda x: x[0])
        FT[k] = [x[0] for x in tmp]
        visit[k] = [x[1] for x in tmp]

    n = len(tickets)
    answer = ['ICN']
    found = False  # 첫 번째 유효 경로 찾으면 멈추기 위한 플래그

    def dfs(cur, depth):
        nonlocal found
        if found:
            return  # 이미 경로 찾았으면 더 이상 탐색할 필요 없음

        # 모든 티켓 사용 완료: n개의 티켓으로 n+1개의 공항 방문
        if depth == n:
            found = True
            return

        if cur not in FT:
            return

        for i, nxt in enumerate(FT[cur]):
            if not visit[cur][i]:
                visit[cur][i] = True
                answer.append(nxt)
                dfs(nxt, depth + 1)
                if found:
                    return
                # 백트래킹
                visit[cur][i] = False
                answer.pop()

    dfs('ICN', 0)
    return answer


'''
항공권 정보가 담긴 2차원 배열 tickets가 주어질 때, 방문하는 공항 경로를 return
경로가 2개 이상인 경우 알파벳 순서가 앞서는 경우로
모든 항공권을 사용해야 함
출발지는 ICN 고정

'''