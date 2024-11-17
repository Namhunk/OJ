import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 한 줄에 모든 조합의 주헌고통지수의 합을 1e9+7로 나눈 나머지 출력

# 메뉴의 총 개수 n
n = int(input().strip())

# n개 메뉴의 스코빌 지수 0 <= arr <= 2e31-1
arr = sorted(list(map(int, input().strip().split())))
mod = int(1e9)+7
# 분할정복
def pow(x, y):
    if y == 0: return 1
    if y == 1: return x

    result = pow(x, y//2)
    return (result * result % mod) if y % 2 == 0 else (result * result * x % mod)

ans = 0
for i in range(n):
    ans += arr[i] * (pow(2, i) - pow(2, n-i-1))

print(ans % mod)

"""
메뉴들의 스코빌 지수에서 최대 수치 - 최소 수치 의 값을 "주헌고통지수" 라고 정의함
2가 최대값 인 경우 = [2]
2가 최소값 인 경우 = [2], [2 5], [2 8], [2 5 8]

5가 최대값 인 경우 = [5], [2, 5]
5가 최소값 인 경우 = [5], [5, 8]

8이 최대값 인 경우 = [8], [2, 8], [5, 8], [2, 5, 8]
8이 최소값 인 경우 = [8]
"""
