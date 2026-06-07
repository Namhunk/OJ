def solution(money):
    n = len(money)
    if n == 1:
        return money[0]

    # 첫 집 포함, 마지막 집 제외
    case1 = find(money[:-1])

    # 첫 집 제외, 마지막 집 포함 가능
    case2 = find(money[1:])

    return max(case1, case2)

def find(arr):
    n = len(arr)
    
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

    return dp[-1]
"""
인접한 두 집을 털면 경보가 울림

이웃한 두 idx 는 포함 불가 0 = (n, 1), 1 = (0, 2)


"""