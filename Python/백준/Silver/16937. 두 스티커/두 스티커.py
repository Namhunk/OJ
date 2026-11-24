import sys
input = sys.stdin.readline

    
def solve():
    pass

def main():
    H, W = map(int, input().strip().split())
    N = int(input().strip())

    arr = []
    for i in range(N): # 1차적으로 가능한 경우를 고름
        R, C = map(int, input().strip().split( ))

        # 조건을 만족하는 값들을 집어넣음
        if R <= H and C <= W:
            arr.append((R, C, R*C, i))

        if C <= H and R <= W:
            arr.append((C, R, R*C, i))

    ans = 0
    for x in range(len(arr)):
        nH, nW = H-arr[x][0], W-arr[x][1]

        for y in range(x+1, len(arr)):
            if arr[x][3] == arr[y][3]: continue

            if arr[y][0] <= nH and arr[y][1] <= W:
                ans = max(ans, arr[x][2] + arr[y][2])

            if arr[y][0] <= H and arr[y][1] <= nW:
                ans = max(ans, arr[x][2] + arr[y][2])

    print(ans)

if __name__ == '__main__':
    main()

"""
H x W 크기의 모눈종이에 N개의 스티커 중 붙일 수 있는 것들을 모두 사용할 때 최대 넓이 
모든 스티커는 사각형

2개의 스티커를 골라 붙임

1. 현재 스티커를 그대로 붙임
    1. 다음 스티커를 그대로 붙임
    2. 다음 스티커를 회전해서 붙임

2. 현재 스티커를 회전해서 붙임
    1. 다음 스티커를 그대로 붙임
    2. 다음 스티커를 회전해서 붙임

2 x 2에 1 x 2 넓이를 제외하면
1 x 2, 2 x 1 이 나옴

10 x 9에 5 x 10을 제외하면 
10 x 4, 0 x 9

10 x 10에 7 x 7 넓이를 제외하면 
3 x 10, 10 x 3 두가지 경우가 나옴

"""