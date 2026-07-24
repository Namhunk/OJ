from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    summits_set = set(summits)
    visit = [float('inf')] * (n + 1)
    heap = []
    for g in gates:
        visit[g] = 0
        heappush(heap, (0, g))

    push, pop = heappush, heappop  # 지역변수 캐싱으로 약간의 속도 이득
    while heap:
        dist, x = pop(heap)
        if dist > visit[x]:
            continue
        if x in summits_set:
            continue  # 산봉우리에서는 더 이상 뻗어나가지 않음
        for w, nx in graph[x]:
            cand = w if w > dist else dist  # max(w, dist)
            if cand < visit[nx]:
                visit[nx] = cand
                push(heap, (cand, nx))

    answer = [(s, visit[s]) for s in summits]
    answer.sort(key=lambda x: (x[1], x[0]))
    return answer[0]
'''
n개의 지점이 존재
각 지점은 1 ~ n의 숫자

출입구에서 산봉우리 한 곳을 방문 후 다시 원래의 출입구로 오는 코스

출입구 -> 산봉우리 의 값들 중 최솟 값을 구하면 알아서 최적값이 나옴

1. 출발지점 부터 산봉우리 까지 이동할 때 사용한 경로 중 최대 intensity가 최소인 경로
'''