import sys
input = sys.stdin.readline

"""
요세푸스 순열 출력

요세푸스 문제:
1 - N 까지 N 명의 사람이 원을 이루면서 앉아있고 K(<= N)이 주어졌을 때 K번째 사람을 제거한다.
이 과정을 N번 반복 
"""

# (1 <= K <= N <= 5,000)
N, K = map(int, input().strip().split())

from collections import deque
que = deque([i for i in range(1, N+1)])

cnt = 1
ans = []
while que:
    if cnt == K:
        cnt = 1
        ans.append(que.popleft())
    else:
        que.append(que.popleft())
        cnt += 1

print('<',end='')
print(*ans, sep=', ', end='')
print('>')