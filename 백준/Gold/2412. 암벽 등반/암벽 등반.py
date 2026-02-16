import sys
input = sys.stdin.readline

from collections import deque
def solve():
    # n (1 <= n <= 50,000), T (1 <= T <= 200,000)
    n, T = map(int, input().strip().split())

    crack = set([tuple(map(int, input().strip().split())) for _ in range(n)])
    que = deque([(0, 0, 0)])
    while que:
        x, y, c = que.popleft()
        if y == T: return c

        for a in range(-2, 3):
            for b in range(-2, 3):
                if (a, b) == (0, 0): continue
                nx, ny = x+a, y+b

                if (nx, ny) in crack:
                    crack.remove((nx, ny))
                    que.append((nx, ny, c+1))
    
    return -1

print(solve())

"""
첫째 줄에 최소 이동 회수를 출력. 만약 정상에 오를 수 없다면 -1 출력

(0, 0)에서 시작

| a-x | <= 2 and | b-y | <= 2 이면 (x, y)에서 (a, b)로 이동 할 수 있다
"""