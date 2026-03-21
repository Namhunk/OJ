import sys
input = sys.stdin.readline

from itertools import product
def solve():
    # N, K (10 <= N <= 100,000,000, 1 <= K 원소의 개수 <= 3)
    N, M = map(int, input().strip().split())
    K = sorted(list(map(int, input().strip().split())))
    
    MAX_SIZE = len(str(N))
    ans = 0
    for SIZE in range(1, MAX_SIZE+1):
        for i in product(K, repeat=SIZE):
            number = int(''.join(map(str, i)))

            if number <= N:
                ans = max(ans, number)
    print(ans)

if __name__ == '__main__':
    solve()

"""
N보다 작거나 같은 자연수 중, 집합 K의 원소로만 구성된 가장 큰 수를 출력
K의 각 원소는 1 - 9 사이의 자연수

K 원소의 개수가 최대 3개 이고 N을 문자로 변환했을때의 길이의 범위가 2 ~ 9이므로
모든 범위를 탐색
"""