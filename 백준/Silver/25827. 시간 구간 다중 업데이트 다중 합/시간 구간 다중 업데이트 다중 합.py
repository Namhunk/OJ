from collections import deque
import sys

# 전체 시간 구간의 초기값은 0, A에 저장된 유형 1의 질의로 값 증가
# 유형 2의 질의로 값 출력
arr = [0]*(24*60*60 + 1)
n = int(sys.stdin.readline().strip())
que = deque()
for _ in range(n):
    q, s, e = sys.stdin.readline().strip().split()
    h1, m1, s1 = map(int, s.strip().split(":"))
    h2, m2, s2 = map(int, e.strip().split(":"))

    s_time = h1*60**2 + m1*60 + s1
    e_time = h2*60**2 + m2*60 + s2

    if int(q) > 1: que.append((s_time, e_time))
    else: arr[s_time+1] += 1; arr[e_time+1] -= 1

for _ in range(2):
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]

for _ in range(len(que)):
    start, end = que.popleft()

    print(arr[end] - arr[start])
