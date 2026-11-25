import sys
import random, math
input = sys.stdin.readline

    
def solve(N, K):
    if K == 1: return 0

    r = 0
    p = 10
    for i in range(1, N+1):
        if i == p:
            p *= 10
        r = (r*p + i) % K

    return r

def main():
    N, K = map(int, input().strip().split())
    print(solve(N, K))

if __name__ == '__main__':
    main()

"""
"""