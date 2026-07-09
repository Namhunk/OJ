# 2 <= n <= 1,000
# 1 <= start <= n
# 1 <= end <= n
# 1 <= len(roads) <= 3,000

from heapq import heappush, heappop

def solution(n, start, end, roads, traps):
    trap_idx = {trap: i for i, trap in enumerate(traps)}
    graph = [[] for _ in range(n + 1)]

    # original=0 : 원래 방향 간선
    # original=1 : 반대 방향 확인용 간선
    for p, q, s in roads:
        graph[p].append((q, s, 0))
        graph[q].append((p, s, 1))

    INF = 10 ** 15
    max_state = 1 << len(traps)
    dist = [[INF] * max_state for _ in range(n + 1)]
    dist[start][0] = 0

    heap = [(0, start, 0)]  # cost, node, state

    while heap:
        cost, cur, state = heappop(heap)

        if cur == end:
            return cost

        if dist[cur][state] < cost:
            continue

        cur_on = False
        if cur in trap_idx:
            cur_on = bool(state & (1 << trap_idx[cur]))

        for nxt, w, original in graph[cur]:
            nxt_on = False
            if nxt in trap_idx:
                nxt_on = bool(state & (1 << trap_idx[nxt]))

            reversed_now = cur_on ^ nxt_on

            # reversed_now == 0 이면 원래 방향만 사용 가능
            # reversed_now == 1 이면 반대 방향만 사용 가능
            if reversed_now != original:
                continue

            next_state = state
            if nxt in trap_idx:
                next_state ^= (1 << trap_idx[nxt])

            next_cost = cost + w
            if next_cost < dist[nxt][next_state]:
                dist[nxt][next_state] = next_cost
                heappush(heap, (next_cost, nxt, next_state))

    return -1

'''
탈출하는데 걸리는 최소 시간
roads = [P, Q, S] P -> Q: S시간

트랩을 밟으면 어떻게 처리할 것인지
시간이 작은 순서대로 처리

'''