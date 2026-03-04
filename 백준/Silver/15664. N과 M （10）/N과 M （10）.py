import sys
input = sys.stdin.readline

from itertools import combinations
def solve():
    global N, M, ans, arr
    # N, M (1 <= N <= M <= 8)
    N, M = map(int, input().strip().split())
    arr = sorted(list(map(int, input().strip().split())))
    ans = set() # 중복 방지

    for i in combinations(arr, M):
        ans.add(i)
    
    for i in sorted(ans):
        print(*i)

if __name__ == '__main__':
    solve()

"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
1. N개의 자연수 중 M개를 고른 수열
2. 고른 수열은 비내림차순이어야 한다
3. 길이가 K인 수열 A가 A[1] <= A[2] <= A[3] <= ... <= A[K]를 만족해야 함

각 수열은 고유해야 함

"""