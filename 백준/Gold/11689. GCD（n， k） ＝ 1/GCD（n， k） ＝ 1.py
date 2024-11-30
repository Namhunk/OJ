import sys
input = sys.stdin.readline

# GCD(n, k) = 1을 만족하는 자연수 1 <= k <= n 의 개수를 출력한다

# 첫째 줄에 자연수 n (1 <= n <= 1e12) 이 주어진다
n = int(input().strip())

def solve(n): # 오일러 피 함수
    ans = n
    p = 2
    while p**2 <= n: # n의 소인수만 탐색
        if n % p == 0: # p가 소인수인 경우
            while n % p == 0:
                n //= p
            ans *= (1 - 1/p)
        p += 1

    if n > 1:
        ans *= (1 - 1/n)
    return int(ans)

print(solve(n))

"""
GCD(n, k) = 1 이려면 n과 k는 서로소 형태 여야 함

"""