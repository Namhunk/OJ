import sys
input = sys.stdin.readline

def solve():
    # 전구의 개수 N, 명령어 개수 M (1 <= N, M <= 4,000)
    N, M = map(int, input().strip().split())

    S = [0] + list(map(int, input().strip().split()))

    # a == 1: (b, c) = (i, x), a > 1: (b, c) = (l, r)
    for _ in range(M):
        a, b, c = map(int, input().strip().split())
        S = Switch(a, b, c, S)

    print(*S[1:])
def Switch(a, b, c, S):
    if a == 1:
        S[b] = c

    elif a == 2: 
        for i in range(b, c+1):
            S[i] ^= 1

    elif a == 3: 
        for i in range(b, c+1):
            S[i] = 0

    else: 
        for i in range(b, c+1):
            S[i] = 1

    return S

if __name__ == '__main__':
    solve()

"""
전구를 제어하는 방법
1. i번 전구를 x 상태로 변경
2. l ~ r 사이의 전구 상태를 반전
3. l ~ r 사이의 전구를 끔
4. l ~ r 사이의 전구를 킴

"""