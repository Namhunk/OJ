import sys
input = sys.stdin.readline

def solve():
    # N (1 <= N <= 50,000)
    N = int(input().strip())

    sky_line = []
    for _ in range(N):
        # (1 <= x <= 1,000,000, 0 <= y <= 500,000)
        x, y = map(int, input().strip().split())
        sky_line.append((x, y))
    
    sky_line = sorted(sky_line, key=lambda x: x[0]) # X축을 기준으로 정렬

    cnt = 0
    stack = [0]
    for x, y in sky_line:
        while stack and stack[-1] > y:
            stack.pop()
            cnt += 1
        
        if stack[-1] < y:
            stack.append(y)
        
    while stack[-1] > 0:
        stack.pop()
        cnt += 1
    
    print(cnt)


if __name__ == '__main__':
    solve()

"""
x, y는 고도가 바뀌는 지점
첫 x의 최표는 1

x, y (1 <= x <= 1,000,000, 0 <= y <= 500,000)
x, y의 범위가 크므로 좌표를 간단하게 나타낼 필요가 있음

총 n개의 숫자들에 대해
1. 첫 고도는 0
2. 
"""