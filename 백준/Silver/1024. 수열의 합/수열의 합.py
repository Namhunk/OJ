import sys
input = sys.stdin.readline

# N과 L이 주어질 때, 합이 N, 길이가 2 <= L <= 100 인 가장 짧은 연속된 음이 아닌 정수 리스트
# 시작 지점이 어딘지 구해야 할때
# 시작 지점이 X 라면
# L(X + (X+(L-1)))) = 2N # 등차 수열의 합
# L(2X+(L-1)) = 2N
# 2X+(L-1) = 2N/L -> 2X = 2N/L - (L-1)
# X = N/L -(L-1)/2 -> X = (2N - L(L-1)) / 2L
# X의 값이 자연수가 나와야 함
N, L = map(int, input().strip().split())
ans = -1
for l in range(L, 101):
    X = N/l - (l-1)/2

    if X == int(X) and X >= 0:
        ans = int(X)
        L = l
        break

if ans != -1: print(*list(range(ans, ans+L)))
else: print(-1)