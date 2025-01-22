import sys
input = sys.stdin.readline

# 늑대가 양이 있는 칸으로 갈 수 없게 할 수 있다면 첫째 줄에 1, 둘째줄에 목장의 상태를 출력 울타리는 'D'로 출력
# 울타리를 어떻게 설치해도 양이 있는 칸으로 갈 수 있다면 첫째 줄에 0을 출력

# 목장의 크기는 R x C

# 목장의 크기 R, C가 주어짐
R, C = map(int, input().strip().split())

# 목장의 상태가 주어짐 '.' = 빈칸, 'S' = 양, 'W' = 늑대
arr = [list(input().strip()) for _ in range(R)]

# 늑대와 양 사이에 빈 공간이 있다면 1, 없다면 0

def solve(R, C, arr):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'S':
                for k in range(-1, 2, 2):
                    if 0 <= i+k < R and arr[i+k][j] == 'W':
                        print(0)
                        return
                    if 0 <= j+k < C and arr[i][j+k] == 'W':
                        print(0)
                        return
            elif arr[i][j] == '.':
                arr[i][j] = 'D'

    print(1)
    for i in arr:
        print(''.join(i))

    return

solve(R, C, arr)