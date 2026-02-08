import sys
input = sys.stdin.readline

"""
각 테스트 케이스마다 다이아몬드의 가치가 높아지는 부분열중 최장의 것의 길이를 구해라

"""

def solve(N, WC):
    arr = [1] * N

    for i in range(1, N):
        for j in range(i):
            if WC[i][0] > WC[j][0] and WC[i][1] < WC[j][1]:
                arr[i] = max(arr[i], arr[j] + 1)
    
    return max(arr)

# 테스트 케이스 개수 T (1 <= T <= 100)
T = int(input().strip())
for _ in range(T):
    # 다이아 정보의 개수 N (1 <= N <= 200)
    N = int(input().strip())

    # [w[i], c[i]](0 <= w[i], c[i] <= 100) w: 무게, c: 선명도
    WC = [list(map(float, input().strip().split())) for _ in range(N)]

    print(solve(N, WC))