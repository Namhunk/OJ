def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        # 1) N을 i번 이어붙인 수
        dp[i].add(int(str(N) * i))

        # 2) j + (i-j) 로 쪼개서 사칙연산
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)

        # 이번 i번 사용해서 만든 수들 중에 number가 있으면 정답
        if number in dp[i]:
            return i

    # 8번 사용까지 못 만들면 -1
    return -1