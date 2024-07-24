import sys
from collections import Counter
input = sys.stdin.readline

# 선분은 양 끝점의 x, y 좌표로 표현
# 두 선분이 서로 만나는 경우, 두 선분은 같은 그룹에 속한다고 정의하며, 그룹의 크기는 그 그룹에 속한 선분의 개수로 정의
# 두 선분이 만난다는 것은 선분의 끝점을 스치듯이 만나는 경우도 포함

def find(x):
    if x != parent[x]: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: parent[y] = x
    else: parent[x] = y

def CCW(x1, y1, x2, y2, x3, y3): # 외적
    return (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)

def isintersect(x1, y1, x2, y2, x3, y3, x4, y4):
    res1 = CCW(x1, y1, x2, y2, x3, y3)
    res2 = CCW(x1, y1, x2, y2, x4, y4)
    res3 = CCW(x3, y3, x4, y4, x1, y1)
    res4 = CCW(x3, y3, x4, y4, x2, y2)

    if res1 == res2 == res3 == res4 == 0:
        if (max(x1, x2) < min(x3, x4)) or (max(x3, x4) < min(x1, x2)) or (max(y1, y2) < min(y3, y3)) or (max(y3, y4) < min(y1, y2)):
            return 0
        else:
            return 1

    elif (res1 * res2 <= 0) and (res3 * res4 <= 0):
        return 1
    else:
        return 0

def fine(x):
    if x != parent[x]: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: parent[y] = x
    else: parent[x] = y

# CCW(Counter Clock Wise)
# 1 <= N <= 3000
N = int(input().strip())
# 양 끝점의 좌표 x1, y1, x2, y2 / 각 좌표의 절대값은 5,000을 넘지 않음
arr = [tuple(map(int, input().strip().split())) for _ in range(N)]
parent = [i for i in range(N)]
ans = N
count = [0]*N

for i in range(N):
    for j in range(i+1, N):
        if isintersect(*arr[i], *arr[j]) and find(i) != find(j):
            union(i, j)
            ans -= 1

for i in range(N):
    count[find(i)] += 1

# 첫째 줄에 그룹의 수, 둘째 줄에 가장 크기가 큰 그룹에 속한 선분의 개수 출력

print(ans)
print(max(count))