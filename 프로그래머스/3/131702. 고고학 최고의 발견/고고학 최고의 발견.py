from itertools import product
from copy import deepcopy

def turn(board, x, y, k, n):
    for r, c in [(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)]:
        nx, ny = x + r, y + c
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] = (board[nx][ny] + k) % 4


def solution(clockHands):
    base = clockHands
    n = len(base)
    answer = float('inf')

    for first_row in product([0, 1, 2, 3], repeat=n):
        cnt = 0
        board = deepcopy(base)

        for c, k in enumerate(first_row):
            if k == 0:
                continue
            turn(board, 0, c, k, n)
            cnt += k

        for r in range(1, n):
            for c in range(n):
                x = board[r - 1][c]
                if x == 0:
                    continue
                need = (4 - x) % 4
                turn(board, r, c, need, n)
                cnt += need

        if all(v == 0 for v in board[-1]):
            answer = min(answer, cnt)

    return answer

'''
한 번의 조작으로 시계방향 90 를 돌릴 수 있음
하나를 돌리면 주위 상하좌우를 같이 돌림

모든 시곗바늘이 12시를 가리키면 해결
최소 조작 횟수를 return

배열의 모든 숫자를 0으로 만드는 최소 조작 횟수
'''