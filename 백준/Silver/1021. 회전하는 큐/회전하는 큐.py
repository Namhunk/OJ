import sys
from collections import deque
input = sys.stdin.readline

# 첫째 줄에 지정한 원소를 뽑아내는데 걸리는 2, 3 연산의 최솟값

# 1. 첫 번째 원소를 뽑아내기 = A[1], A[2], ..., A[k] -> A[2], ..., A[k]
# 2. 왼쪽으로 한 칸 이동 = A[1], A[2], ..., A[k] -> A[2], .., A[k], A[1]
# 3. 오른쪽으로 한칸 이동 = A[1], A[2], ..., A[k] -> A[k], A[1], .., A[k-1]

# 큐의 크기 N(1 <= N <= 50), 뽑아내려고 하는 수의 개수 M(1 <= M <= N)
N, M = map(int, input().strip().split())

# 뽑아내려고 하는 수의 위치
A = list(map(int, input().strip().split()))
que = deque(range(1, N+1))
cnt = 0
for i in A:
    while True:
        if i == que[0]:
            que.popleft()
            break
        else:
            if que.index(i) <= len(que)//2:
                que.rotate(-1)
                cnt += 1
            else:
                que.rotate(1)
                cnt += 1

print(cnt)