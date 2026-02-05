import sys
input = sys.stdin.readline

"""
첫 번째 줄에 탈출에 필요한 최소의 버튼 횟수 출력
탈출할 수 없다면 "ANG"를 따옴표 없이 출력

1. A를 누르면 N+1
2. B를 누르면 N*2(ex: 123 -> 246 -> 146, 5 -> 10 -> 0, 3 -> 6 -> 5)
3. if N > 99,999 -> "ANG"
4. B를 눌러 N에 2를 곱한 순간 N이 99,999를 넘긴다면, 높은 자릿수의 수를 1 낮췄을때, 99,999를 넘지 않는다 해도 "ANG"

- 최대 T회 버튼 사용 가능
- 그 횟수 안에 N값을 G와 같게 만들어야 탈출
"""

MAX_NUM = 99_999

def button_A(N, CNT): # False: MAX값 넘김
    X = N+1

    if X > MAX_NUM: return X, CNT+1, False
    else: return X, CNT+1, True

def button_B(N, CNT):
    if N == 0: return N, CNT+1, True # N이 0인 경우 바로 반환
    X = N * 2

    if X > MAX_NUM: return X, CNT+1, False
    else:
        size = len(str(X))-1
        X = X - 10**size
        return X, CNT+1, True

from collections import deque
def solve(N, T, G):
    visit = [1]*(MAX_NUM+1) # 목표 숫자의 크기만한 배열
    visit[N] = 0 # 현재 N위치 방문 처리

    que = deque([(N, 0)])
    while que:
        X, CNT = que.popleft()

        if X == G: return CNT # 현재 숫자가 목표 숫자와 같다면 횟수 반환
        if CNT >= T: continue # 현재 횟수가 T 이상인 경우 실행 x

        A_X, A_CNT, A_FLAG = button_A(X, CNT)
        if A_FLAG and visit[A_X]:
            visit[A_X] = 0
            que.append((A_X, A_CNT))
        
        B_X, B_CNT, B_FLAG = button_B(X, CNT)
        if B_FLAG and visit[B_X]:
            visit[B_X] = 0
            que.append((B_X, B_CNT))

    return "ANG"

# N(0 <= N <= 99,999), T(1 <= T <= 99,999), G(0 <= G <= 99,999)
N, T, G = map(int, input().strip().split())
print(solve(N, T, G))