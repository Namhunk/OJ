import sys
input = sys.stdin.readline

"""
비어있는 정원에서 좌표 (a, b)에 트릭 플라워를 심었을 때 적어도 몇 초가 지나야 
한 좌표에 두 송이의 꽃이 피는지

1. 처음에 트릭 플라위의 좌표를 (0, 0)에 심음  이때 꽃의 좌표는 x[0], y[0]
2. t 초가 지난 뒤 피어나는 꽃의 좌표는 x[t], y[t]
3. if (x[t]+1) + (y[t]+1) < R 인경우 x[t+1], y[t+1] = x[t]+1, y[t]+1임
4. 그렇지 않다면 x[t+1], y[t+1] = x[t] // 2, y[t] // 2 이다

"""

# a, b 입력 (0 <= a, b <= R) 트릭 플라워의 시작점
a, b = map(int, input().strip().split())

# R 입력 (1 <= R <= 10**3)
R = int(input().strip())

visit = [[0]*R for _ in range(R)]
visit[a][b] = 1

from collections import deque
que = deque([(a, b)])
cnt = 0

while 1:
    x, y = que.popleft()
    
    if visit[x][y] == 2: break

    if (x+1) + (y+1) < R:
        visit[x+1][y+1] += 1
        que.append((x+1, y+1))
    else:
        visit[x//2][y//2] += 1
        que.append((x//2, y//2))
    
    cnt += 1
    
print(cnt)