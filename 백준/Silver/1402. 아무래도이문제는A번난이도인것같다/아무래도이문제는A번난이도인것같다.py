import sys
input = sys.stdin.readline

# 각 테스트 케이스마다 한 줄에 변할 수 있으면 yes, 아니면 no 출력

# 테스트 케이스 T (1 <= T <= 100)
T = int(input().strip())

# 테스트 케이스마다 두 정수 A, B (-2^31 <= A, B <= 2^31-1)가 주어진다
for _ in range(T):
    A, B = map(int, input().strip().split())
    print('yes')

"""
A = A * 1 -> A + 1
A = A * 1 * -1 * -1 -> A + 1 - 1 -1 = A - 1
어떤 수가 와도 변할 수 있다
"""
