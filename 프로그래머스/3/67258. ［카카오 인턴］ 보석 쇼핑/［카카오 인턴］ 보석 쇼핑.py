from collections import defaultdict

def solution(gems):
    n = len(gems)
    total = len(set(gems))  # 필요한 보석 종류 수

    counter = defaultdict(int)
    left = 0
    best_len = n + 1
    best_l, best_r = 0, 0  # 0-index 기반

    distinct = 0  # 현재 윈도우 안의 서로 다른 보석 수

    for right in range(n):
        gem = gems[right]
        counter[gem] += 1
        if counter[gem] == 1:
            distinct += 1

        # 모든 종류를 다 포함하고 있다면 left를 최대한 줄여본다
        while distinct == total:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_l, best_r = left, right

            # left를 하나 줄여본다
            left_gem = gems[left]
            counter[left_gem] -= 1
            if counter[left_gem] == 0:
                distinct -= 1
            left += 1

    # 문제에서 1-based index를 요구
    return [best_l + 1, best_r + 1]