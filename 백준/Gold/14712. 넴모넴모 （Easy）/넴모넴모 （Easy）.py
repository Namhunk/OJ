import sys
input = sys.stdin.readline

def solve():
    global N, M, ans, arr
    # 행 N, 열 M (1 <= N, M <= 25, 1 <= N x M <= 25)
    N, M = map(int, input().strip().split())

    arr = [[0]*(M) for _ in range(N)]
    ans = 0
    dfs(0)
    print(ans)

def dfs(idx):
    global ans
    if idx == N*M:
        ans += 1
        return
    
    r = idx // M
    c = idx % M

    arr[r][c] = 0
    dfs(idx+1)

    arr[r][c] = 1
    if not check(r, c):
        dfs(idx + 1)
    
    arr[r][c] = 0

def check(r, c):
    if r == 0 or c == 0: return 0
    return arr[r][c] and arr[r-1][c] and arr[r][c-1] and arr[r-1][c-1]

if __name__ == '__main__':
    solve()
"""
N x M 의 격자가 있을떄
2 x 2가 되지 않는 모든 배치의 가짓수

N x M <= 25 이므로 완전탐색을 수행

"""