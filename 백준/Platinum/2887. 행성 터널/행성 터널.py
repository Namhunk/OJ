import sys
input = sys.stdin.readline

# 첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.

# 행성의 개수 N (1 <= N <= 100,000)
N = int(input().strip())

# N개의 줄에 주어지는 각 행성의 x, y, z 좌표(-1e9 <= x,y,z <= 1e9) 행성의 위치는 겹치지 않음
planet = []
for i in range(N):
    points = list(map(int, input().strip().split())) + [i] # 행성의 좌표, 번호 저장
    planet.append(tuple(points))
# 행성은 3차원 좌표위의 한 점, 두 행성 A(xA, yA, zA), B(xB, yB, zB)를 터널로 연결할 때 드는 비용은
# min(|xA-xB|, |yA-yB|, |zA-zB|)

# Kruskal mst

# union-find
parents = list(range(N))
def find(x):
    if x != parents[x]: parents[x] = find(parents[x])
    return  parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: x, y = y, x

    parents[x] = y

dist = [] # 좌표의 거리 저장 배열
for j in range(3):
    planet.sort(key=lambda x: x[j]) # 각 좌표의 크기별로 정렬
    for i in range(1, N):
        # 거리, 행성1, 행성2
        dist.append((abs(planet[i-1][j]-planet[i][j]), planet[i-1][3], planet[i][3]))

dist.sort() # 거리가 가까운 순으로 정렬

ans = 0
cnt = 0
for d, x, y in dist:
    x, y = find(x), find(y)
    if x != y:
        union(x, y)
        cnt += 1
        ans += d

    if cnt >= N-1: break
    
print(ans)