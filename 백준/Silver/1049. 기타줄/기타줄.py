import sys
input = sys.stdin.readline

# 끊어진 기타줄의 개수 N, 기타줄 브랜드 M
# 적어도 N개를 사기 위해 필요한 돈의 수를 최소로

# N (1 <= N <= 100), M (1 <= M <= 50)
N, M = map(int, input().strip().split())

A, B = [], [] # A: 패키지 가격, B: 낱개 가격

for i in range(M):
    a, b = map(int, input().strip().split())
    A.append(a)
    B.append(b)

package = min(A) # 패키지 가격 중 가장 싼 가격
piece = min(B) # 낱개 가격 중 가장 싼 가격

# 1. N > 6인 경우 패키지 or 낱개 중 N // 6 개를 구매할 때 더 값싼 물건을 구매
cost = package * (N // 6) if package * (N // 6) < piece * 6 * (N // 6) else piece * 6 * (N // 6)

# 2. 나머지 N % 6개 중 패키지 1개 or 낱개 N % 6개 가격 중 최솟값
cost += package if package < piece * (N % 6) else piece * (N % 6)

print(cost)