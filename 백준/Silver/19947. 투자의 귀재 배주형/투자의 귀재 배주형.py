import sys
input = sys.stdin.readline

def solve():
    # 초기비용 H, 투자 기간 Y
    H, Y = map(int, input().strip().split())
    
    arr = [[H]*(3) for _ in range(Y+1)]

    for i in range(1, Y+1):
        if i < 1: continue
        # 1년에 5%
        arr[i][0] = int(max(f1(arr[i-1][0]), f1(arr[i-1][1]), f1(arr[i-1][2])))

        if i < 3: continue
        # 3년에 20%
        arr[i][1] = int(max(f2(arr[i-3][0]), f2(arr[i-3][1]), f2(arr[i-3][2])))

        if i < 5: continue
        # 5년에 35%
        arr[i][2] = int(max(f3(arr[i-5][0]), f3(arr[i-5][1]), f3(arr[i-5][2])))
    
    print(max(arr[-1]))

    
def f1(x):
    return x + x*0.05

def f2(x):
    return x + x*0.2

def f3(x):
    return x + x*0.35
if __name__ == '__main__':
    solve()

"""
투자의 방법
1년에 5%
3년에 20%
5년에 35%

H원을 Y년 투자한다 할 때
Y가 크지 않으므로

모든 방법을 구하면 될 것 같음

"""