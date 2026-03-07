import sys
input = sys.stdin.readline

def solve():
    # n, m (1 <= n, m <= 1,000)
    n, m = map(int, input().strip().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip())))

    ans = 0
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

            ans = max(ans, dp[i][j])

    
    return ans **2
    

if __name__ == '__main__':
    print(solve())

"""
nxm의 0, 1 로 된 배열이 있을때
이 배열에서 1로 된 가장 큰 정사각형의 넓이를 구하는 프로그램

정사각형이 되려면 높이, 밑변의 길이가 같아야 함

if arr[i][j] == 1: 최소 크기의 정사각형
이떄 arr[i-1][j], arr[i][j-1], arr[i-1][j-1] 3개의 값이 1이라면 정사각형을 만족함
또한 모든 정답은 K^2 꼴 (K = 1, 2, ...1000)

1. n x m 의 배열에서 정확히 어떤 범위에 정사각형이 존재하는지 모름
2. 정사각형이 되려면 최소 현재 위치는 1값을 가져야 함
3. arr[i-1][j-1], arr[i-1][j], arr[i][j-1] 3값이 모두 0보다 커야함
4. 3번의 3개 값이 모두 1일때 한 변의 길이는 + 1임


4 4
0100
0111
1110
0010

4 4
0100
0111
1111
0111

"""