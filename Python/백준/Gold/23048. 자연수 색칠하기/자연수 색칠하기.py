import sys
input = sys.stdin.readline

def solve(N):
    colors = [0, 1] + [0]*(N-1)
    cnt = 1
    for i in range(2, N+1):
        if colors[i] == 0:
            cnt += 1
            for j in range(i, N+1, i):
                if colors[j] == 0:
                    colors[j] = cnt

    print(cnt)
    print(*colors[1:])

def main():
    # N(1 <= N <= 500,000)
    N = int(input().strip())

    solve(N)



if __name__ == '__main__':
    main()
"""
1 ~ N 까지의 자연수를 색칠
단, 서로소인 서로 다른 두 자연수는 다른색으로 색 칠
최소한의 색을 써서 모든 자연수를 칠하는 방법을 찾아라

사용한 색상의 수 K 출력
N개의 수를 공백을 사이에 두고 출력

---------------------------------

각 최소 공약수들에 색상을 지정
"""