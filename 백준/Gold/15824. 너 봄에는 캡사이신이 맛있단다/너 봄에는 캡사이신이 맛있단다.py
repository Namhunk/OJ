import sys
input = sys.stdin.readline

# 한 줄에 모든 조합의 주헌고통지수의 합을 1e9+7로 나눈 나머지 출력

# 메뉴의 총 개수 n
n = int(input().strip())

# n개 메뉴의 스코빌 지수 0 <= arr <= 2e31-1
arr = sorted(list(map(int, input().strip().split())))
mod = int(1e9)+7

ans = 0
for i in range(1, n):
    for j in range(i):
        ans = (ans+(arr[i]-arr[j])*(2**(i-j-1))) % mod

print(ans)

"""
메뉴들의 스코빌 지수에서 최대 수치 - 최소 수치 의 값을 "주헌고통지수" 라고 정의함
1 4 5 5 6 10

1 4 = 2^0
1 5, 1 4 5 = 2^1
1 5, 1 4 5, 1 5 5, 1 4 5 5 = 2^2
1 6, 1 4 6, 1 5 6, 1 5 6, 1 4 5 6, 1 5 5 6, 1 4 5 6, 1 4 5 5 6 = 2^3
.
.
. = 2^4

"""
