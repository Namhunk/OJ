import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 스브러스가 어른들에게 들키지 않고 아이들로부터 뺏을 수 있는 최대 사탕의 수

# 스브러스는 한 아이의 사탕을 뺏으면 그 아이 친구들의 사탕도 뺏음
# 아이가 사탕을 뺏기면 울고, K명의 아이가 울면 공명해 어른들이 나옴

# 거리에 있는 아이들 수 N(1 <= N <= 30,000),
# 아이들의 친구 관계 수 M(1 <= M <= 100,000),
# 울음 소리가 공명하기 위한 최소 아이의 수 K(1 <= K <= min{N, 3,000})
N, M, K = map(int, input().strip().split())
parent = [i for i in range(N+1)] # 친구 관계를 표시할 배열

# 아이들이 받은 사탕의 수 c[i](1 <= c[i] <= 10,000)
c = [0] + list(map(int, input().strip().split()))

# union - find
def find(x):
    if x != parent[x]: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: x, y = y, x # x 값이 큰 숫자가 나오게
    parent[x] = y # x위치에 y값 저장

# M개의 줄에 각 정수 a, b (1 <= a,b <= N, a != b)
for _ in range(M):
    a, b = map(int, input().strip().split())
    union(a, b) # 아이들의 친구 표시

group = [0]*(N+1) # 친구 그룹을 하나로 통일
for i in range(1, N+1):
    if i != parent[i]:
        idx = find(i)
        group[idx] += 1
        c[idx] += c[i] # 총 사탕 수
    else:
        group[i] += 1

# 배낭 문제?
# 각 아이가 가진 사탕의 수 -> 가치, 울음 소리가 공명하기 위한 최소 아이의 수 K -> 무게
dp = [0]*K # K를 넘으면 안됨
for i in  range(1, N+1):
    if group[i] == 0: continue
    W, V = group[i], c[i]

    if W >= K: continue
    for j in range(K, -1, -1):
        if j + W < K and dp[j] != 0:
            dp[j+W] = max(dp[j+W], dp[j]+V)

    dp[W] = max(dp[W], V)

print(max(dp))