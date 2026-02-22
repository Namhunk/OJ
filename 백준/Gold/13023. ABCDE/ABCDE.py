import sys
input = sys.stdin.readline

def f(x, cnt):
    if cnt == 5: return 1

    ans = 0
    for nx in friends[x]:
        if visit[nx]: continue
        visit[nx] = cnt
        ans = max(ans, f(nx, cnt+1))
        visit[nx] = 0
    
    return ans



def solve():
    global friends, visit

    # 사람의 수 N(5 <= N <= 2000), 친구 관계의 수 M (1 <= M <= 2000)
    N, M = map(int, input().strip().split())

    friends = [[] for _ in range(N)]
    # a, b는 친구 (0 <= a, b <= N-1, a != b)
    for _ in range(M):
        a, b = map(int, input().strip().split())
        friends[a].append(b)
        friends[b].append(a)
    
    visit = [0]*N

    for i in range(N):
        visit[i] = 1
        if f(i, 1): return 1
        visit[i] = 0
    return 0


if __name__ == '__main__':
    print(solve())

"""
문제는 결국 서로 다른 5명 A, B, C, D, E가 각각 친구가 되는
4개의 경로가 있는지 묻는 문제

예제 1
0-1-2-3-4

예제 2
4-1-2-3-0

예제 3
5-3-4-7-1

"""