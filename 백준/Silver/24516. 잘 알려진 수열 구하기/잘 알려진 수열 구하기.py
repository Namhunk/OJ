import sys
input = sys.stdin.readline

# 첫째 줄에 문제 조건에 맞는 길이 N인 수열을 아무거나 출력한다

# 1. 수열의 모든 원소는 서로 다르고, 수열의 원소는 1이상 100,000 이하인 정수다
# 2. 수열의 연속한 부분 수열 중에, 길이가 K인 모든 연속한 부분 수열의 합은 K로 나누어 떨어진다

# 수열의 길이 N (1 <= N <= 5000)
N = int(input().strip())

ans = [i for i in range(1, 2*N, 2)]
print(*ans)
"""
"""
