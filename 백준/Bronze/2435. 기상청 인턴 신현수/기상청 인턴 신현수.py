import sys
input = sys.stdin.readline

def solve():
    # N (2 <= N <= 100, 1 <= K <= N)
    N, K = map(int, input().strip().split())

    # (-100 <= T[i] <= 100)
    T = list(map(int, input().strip().split()))

    for i in range(1, N):
        T[i] = T[i] + T[i-1]
    
    
    ans = T[K-1]
    for i in range(K, N):
        ans = max(ans, T[i] - T[i-K])
    
    print(ans)

if __name__ == '__main__':
    solve()

"""

측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도합이 가장 큰 값
"""