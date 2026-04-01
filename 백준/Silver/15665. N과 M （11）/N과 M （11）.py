import sys
input = sys.stdin.readline

from itertools import product
def solve():
    # N, M (1 <= M <= N <= 7)
    N, M = map(int, input().strip().split())
    
    # arr[i] (1 <= arr[i] <= 10,000)
    arr = sorted(set(map(int, input().strip().split())))

    for i in product(arr, repeat=M):
        print(*i)

if __name__ == '__main__':
    solve()

"""
길이가 M인 수열을 모두 구해라

N개의 자연수 중 M개를 고른 수열
같은 수를 여러 번 골라도 됨

"""