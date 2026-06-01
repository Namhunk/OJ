from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    idx = list(range(n))
    max_win = -1
    best_A = None

    # A가 가져갈 주사위 조합들
    for A in combinations(idx, n // 2):
        B = [i for i in idx if i not in A]

        # A, B의 합의 모든 경우의 수
        sum_As = []
        sum_Bs = []

        for case in product(range(6), repeat=n // 2):
            sA = sum(dice[a][i] for a, i in zip(A, case))
            sB = sum(dice[b][i] for b, i in zip(B, case))
            sum_As.append(sA)
            sum_Bs.append(sB)

        sum_As.sort()
        sum_Bs.sort()

        # A가 이기는 횟수 계산
        win = 0
        for a in sum_As:
            win += bisect_left(sum_Bs, a)

        if win > max_win:
            max_win = win
            best_A = A

    # 1-based 인덱스로 반환
    return [x + 1 for x in best_A]