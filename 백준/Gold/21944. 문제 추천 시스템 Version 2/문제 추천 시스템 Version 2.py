import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def solve():
    # 난이도별 문제 관리 (1 ~ 100)
    l_max = [[] for _ in range(101)]  # 최대 힙
    l_min = [[] for _ in range(101)]  # 최소 힙
    
    # 알고리즘 분류별 문제 관리
    g_max = {}  # 최대 힙
    g_min = {}  # 최소 힙
    
    # 문제의 현재 상태(난이도, 분류)를 저장. O(1) 접근 및 지연 삭제용
    problems = [0] * 100001 
    
    N = int(input())
    for _ in range(N):
        P, L, G = map(int, input().split())
        problems[P] = [L, G]
        
        heappush(l_max[L], -P)
        heappush(l_min[L], P)
        
        if G not in g_max:
            g_max[G] = []
            g_min[G] = []
        heappush(g_max[G], (-L, -P))
        heappush(g_min[G], (L, P))
        
    M = int(input())
    for _ in range(M):
        cmd, *data = input().split()
        
        if cmd == "recommend":
            G, x = map(int, data)
            if x == 1:
                while g_max[G]:
                    L, P = heappop(g_max[G])
                    P = -P
                    L = -L
                    # 삭제되었거나(0) 정보가 업데이트되어 현재 상태와 다르면 버림
                    if not problems[P] or problems[P] != [L, G]:
                        continue
                    print(P)
                    # 유효한 값이므로 다시 힙에 넣음
                    heappush(g_max[G], (-L, -P))
                    break
            else:
                while g_min[G]:
                    L, P = heappop(g_min[G])
                    if not problems[P] or problems[P] != [L, G]:
                        continue
                    print(P)
                    heappush(g_min[G], (L, P))
                    break

        elif cmd == "recommend2":
            x = int(data[0])
            found = False
            if x == 1:
                for L in range(100, 0, -1):
                    while l_max[L]:
                        P = -heappop(l_max[L])
                        if not problems[P] or problems[P][0] != L:
                            continue
                        print(P)
                        heappush(l_max[L], -P)
                        found = True
                        break
                    if found: break
            else:
                for L in range(1, 101):
                    while l_min[L]:
                        P = heappop(l_min[L])
                        if not problems[P] or problems[P][0] != L:
                            continue
                        print(P)
                        heappush(l_min[L], P)
                        found = True
                        break
                    if found: break

        elif cmd == "recommend3":
            x, L_target = map(int, data)
            found = False
            if x == 1:
                for L in range(L_target, 101):
                    while l_min[L]:
                        P = heappop(l_min[L])
                        if not problems[P] or problems[P][0] != L:
                            continue
                        print(P)
                        heappush(l_min[L], P)
                        found = True
                        break
                    if found: break
                if not found:
                    print(-1)
            else:
                for L in range(L_target - 1, 0, -1):
                    while l_max[L]:
                        P = -heappop(l_max[L])
                        if not problems[P] or problems[P][0] != L:
                            continue
                        print(P)
                        heappush(l_max[L], -P)
                        found = True
                        break
                    if found: break
                if not found:
                    print(-1)

        elif cmd == "add":
            P, L, G = map(int, data)
            problems[P] = [L, G]  # 문제 정보 갱신
            
            heappush(l_max[L], -P)
            heappush(l_min[L], P)
            
            if G not in g_max:
                g_max[G] = []
                g_min[G] = []
            heappush(g_max[G], (-L, -P))
            heappush(g_min[G], (L, P))

        elif cmd == "solved":
            P = int(data[0])
            problems[P] = 0  # 문제 비활성화 처리

if __name__ == "__main__":
    solve()