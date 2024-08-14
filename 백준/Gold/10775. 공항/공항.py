import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
# 승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력

# 공항에는 G개의 게이트가 있으며, 1 ~ G까지의 번호가 있음
# 공항에는 P개의 비행기가 순서대로 도착할 예정
# i번째 비행기를 1 ~ g[i] (1 <= g[i] <= G)번째 게이트중 하나에 영구적으로 도킹하려 함
# 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄, 이후 어떤 비행기도 도착 x

# 게이트의 수 G (1 <= G <= 1e5)
G = int(input().strip())

# 비행기의 수 P (1 <= P <= 1e5)
P = int(input().strip())

# P개의 줄에 주어지는 g[i] (1 <= g[i] <= G) 각 비행기는 1 ~ g[i] 사이에 하나에 도킹해야함
# Union-Find를 사용
parents = [i for i in range(G+1)] # 현재 1 ~ g[i] 범위에 어느 게이트가 비어있는지 확인하기 위한 배열
visit = [False] + [True]*G # 방문 표시

def find(x):
    if x != parents[x]: parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = parents[x], parents[y]

    if x < y: x, y = y, x
    parents[x] = y

cnt = 0 # 도킹한 비행기의 수
for _ in range(P):
    g = find(int(input().strip())) # 1 ~ g[i] 범위에 비어있는 게이트를 찾음

    if visit[g] == False: break # 범위 내의 모든 게이트의 자리가 없다면 종료
    visit[g] = False # 방문표시
    union(g-1, g) # 다음 위치의 게이트를 표시
    cnt += 1

print(cnt)