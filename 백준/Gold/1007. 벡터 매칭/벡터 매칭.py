import sys
input = sys.stdin.readline
from itertools import combinations
# 각 테스트 케이스마다 정답을 출력 절대/상대 오차는 10^-6까지 허용

# 테스트 케이스의 개수 T
T = int(input().strip())

def solve():
    # 점의 개수 N, N은 짝수(1 <= N <= 20)
    N = int(input().strip())

    x, y = [0]*N, [0]*N
    for i in range(N):
        x[i], y[i] = map(int, input().strip().split()) # 점의 좌표 (|a. b| <= 100,000), 모든 점은 서로 다름

    ans = float('inf')
    # 벡터는 (x**2 + y**2)**0.5

    sumX = sum(x)
    sumY = sum(y)

    arr = list(combinations(range(N), N//2)) 
    for i in arr[:len(arr)//2]:
        leftX = 0
        leftY = 0
        for j in i:
            leftX += x[j]
            leftY += y[j]

        rightX = sumX - leftX
        rightY = sumY - leftY
        ans = min(ans, ((rightX - leftX) ** 2 + (rightY - leftY) ** 2) ** 0.5)

    return ans


for _ in range(T):
    print(solve())