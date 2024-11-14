import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 친구 관계 트리가 주어졌을 때, 모든 개인이 새로운 아이디어를 수용하기 위하여 필요한 최소 얼리 어답터의 수를 구해라

# 친구 관계 트리의 정점 개수 N (2 <= N <= 1,000,000)
N = int(input().strip())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().strip().split())
    tree[u].append(v)
    tree[v].append(u)

# 각 노드에 대해서 현재 노드가 얼리 어답터인 경우, 아닌 경우로 나눠 생각해봄
visited = [0]*(N+1) # 방문 배열
dp = [[0, 1] for _ in range(N+1)] # 각 노드에 대해서 얼리 어답터의 수 기록

def solve(x):
    visited[x] = 1 # 해당 노드 방문 표시
    if len(tree[x]) == 1: # 리프 노드인 경우
        dp[x] = [0, 1] # 얼리 어답터 x, 얼리 어답터 o

    for i in tree[x]:
        if visited[i]: continue # 방문을 하지 않은 경우
        visited[i] = 1
        solve(i)
        dp[x][0] += dp[i][1] # 현재 노드가 얼리 어답터가 아니라면 이전 노드는 얼리 어답터 이어야 함
        dp[x][1] += min(dp[i]) # 현재 노드가 얼리 어답터라면 이전 노드의 기록 중 더 적은 수를 더함

solve(1)
print(min(dp[1]))