import sys
input = sys.stdin.readline

from math import ceil
def solve():
    # n (0 <= N < 2^63)
    n = int(input().strip())

    q = ceil(n**0.5)
    
    while q**2 < n:
        q += 1
    
    print(q)

if __name__ == '__main__':
    solve()

"""
정수가 주어지면 그 수의 정수 제곱근을 구해라

q^2 >= n인 가장 작은 음이 아닌 정수를 출력

"""