import sys
input = sys.stdin.readline

def solve():
    # R, C, W (2 <= R+W <= 30, 2 <= C+W <= 30, 1 <= W <= 29, C <= R)
    R, C, W = map(int, input().strip().split())

    # 삼각형 생성
    arr = [[0]*32 for _ in range(32)]
    # 첫 위치들 0
    for i in range(1, 31):
        arr[i][1] = 1
        arr[1][i] = 1
    
    for i in range(2, 31):
        for j in range(2, 31):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    
    start = R - C + 1
    ans = 0
    for i in range(W):
        for c in range(C, C+W-i):
            ans += arr[start + i][c]
    
    print(ans)

if __name__ == '__main__':
    solve()

"""
1   1   1   1   1   
1   2   3   4   5   
1   3   6   10  15    
1   4   10  20  35
1   5   15  35  70

위 사각형을 돌리면 삼각형의 모양이 나옴
찾고있는 정삼각형의 윗 꼭짓점은 R행 C번째

만약 R = 2 C = 2 라면

arr[2][2] = 2 인데
실제로는 arr[1][2] = 1위치 부터 해야함
    
2 2 -> 1 2
3 3 -> 1 3
3 2 -> 2 2
R - C + 1 위치부터 시작하도록

또한 R이 1씩 커질수록 C의 범위는 1씩 감소
for i in range(W):
    for c in range(C, C+W-i)
        ans += arr[start+i][c]


"""