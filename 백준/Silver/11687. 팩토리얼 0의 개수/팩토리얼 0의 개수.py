import sys
input = sys.stdin.readline

def f(n):
    cnt = 0
    p = 5

    while p <= n:
        cnt += (n // p)
        p *= 5
    
    return cnt

def solve():
    # M (1 <= M <= 100,000,000)
    M = int(input().strip())

    l, r = 0, 5*10**8
    while l < r:
        m = (l + r) // 2

        if f(m) >= M: r = m
        else: l = m+1
    
    return l if f(l) == M else -1

if __name__ == '__main__':
    print(solve())
    

"""
- 가장 끝의 0의 개수가 M개인 N! 중 가장 작은 N을 찾아라

5의 거듭제곱에 따라 개수가 늘어남

"""