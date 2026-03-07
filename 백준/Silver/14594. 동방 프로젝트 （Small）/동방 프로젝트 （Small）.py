import sys
input = sys.stdin.readline

# def find(x):
#     if x != parent[x]:
#         parent[x] = find(parent[x])
    
#     return parent[x]

def union(x, y):
    # x, y = find(x), find(y)

    if x < y: x, y = y, x
    parent.remove(x)

def solve():
    global parent
    # 동아리 방의 개수 N(2 <= N <= 100)
    N = int(input().strip())

    parent = set([i for i in range(1, N+1)])

    # 빌런의 행동 횟수 M(0 <= M <= 100)
    M = int(input().strip())

    # M번의 행동 x번 방부터 y번 방 사이의 벽을 무너뜨림
    for _ in range(M):
        x, y = map(int, input().strip().split())

        for i in range(x+1, y+1):
            if i not in parent: continue
            union(x, i)

    return len(parent)

if __name__ == '__main__':
    print(solve())

"""
N개의 방은 일직선상에 존재, 왼쪽 1번 오른쪽 N번, 각 방에는 벽 존재

규칙
1. x < y를 만족하는 두 방에 대해서 x부터 y사이에 있는 모든 벽을 허문다
2. 두 방 사이의 벽이 허물어 지면 두 방은 하나로 합쳐짐
3. 이미 허물어진 벽이 존재하면 무시하고 다음 벽을 허문다

남은 동아리 방의 수를 구해라

[1, 2, 3, 4, 5, 5, 5, 5]
"""