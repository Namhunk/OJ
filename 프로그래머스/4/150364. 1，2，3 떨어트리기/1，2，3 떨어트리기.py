def solution(edges, target):
    n = len(target)
    graph = [[] for _ in range(n+1)]
    for a, b in edges:
        graph[a].append(b)
    for i in range(1, n+1):
        graph[i].sort()

    path = [0]*(n+1)       # 각 노드에서 다음에 보낼 자식 인덱스
    visit = [0]*(n+1)      # 리프별 방문(공 개수)
    seq = []               # 공을 떨어뜨렸을 때 도착한 리프 번호 순서

    def drop():
        cur = 1
        while graph[cur]:  # 리프가 아닐 동안
            idx = path[cur]
            nxt = graph[cur][idx]
            path[cur] = (path[cur] + 1) % len(graph[cur])
            cur = nxt
        return cur  # 리프 번호

    # 공을 하나씩 떨어뜨리면서, 언제 멈출지 조건을 제대로 잡기
    while True:
        leaf = drop()
        visit[leaf] += 1
        seq.append(leaf)

        impossible = False
        done = True
        for i in range(1, n+1):
            t = target[i-1]
            c = visit[i]

            if t == 0:
                if c > 0:      # 공이 오면 0을 못 만들기 때문에 바로 불가능
                    impossible = True
                    break
                continue

            if c == 0 and t > 0:
                done = False   # 아직 공이 안 왔으니 더 떨어뜨려야 함
                continue

            if c > t:
                impossible = True   # 공이 너무 많아진 경우, 전부 1이어도 t 초과 → 영원히 불가능
                break

            if t > 3 * c:
                done = False   # 아직 공이 부족 → 더 떨어뜨려야 함

        if impossible:
            return [-1]
        if done:
            break

    # 여기까지 오면 visit[i]는 확정된 공 개수
    # 이제 각 리프에 대해 target을 만족시키도록 1,2,3을 배치
    nums = [[] for _ in range(n+1)]

    for i in range(1, n+1):
        t = target[i-1]
        c = visit[i]
        if t == 0 and c == 0:
            continue
        if c == 0 and t > 0:
            return [-1]

        # c <= t <= 3c 조건은 위에서 이미 만족된 상태라고 가정
        base = c
        remain = t - base   # 1로 c개 깔고, 남는 합을 2/3로 채우기

        arr = [1]*c
        idx = c - 1
        while remain >= 2:
            arr[idx] = 3
            remain -= 2
            idx -= 1
        if remain == 1:
            arr[idx] = 2

        # seq대로 뽑을 때 사전순 최소가 되도록, 뒤에서 pop할 수 있게 뒤집어 둠
        nums[i] = arr[::-1]

    answer = []
    for leaf in seq:
        if not nums[leaf]:
            return [-1]
        answer.append(nums[leaf].pop())

    return answer