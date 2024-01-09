import sys

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
# N개의 자연수는 모두 다른 수

# 1. N개의 자연수 중에서 M개를 고른 수열
# 2. 같은 수를 여러 번 골라도 된다
# 3. 고른 수열은 비내림차순이어야 한다
# (길이가 K인 수열 A가 A1 <= A2 <= A3 <= .. <= Ak를 만족하면, 비내림차순이라 함)

# 조건을 만족하는 수열을 출력, 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력
# 수열은 사전 순으로 증가하는 순서로 출력

def print_seq(seq, x, cnt): # 수열 출력, seq = 수열, x = 시작위치, cnt = 길이
    if cnt == M: print(*seq)
    else:
        for i in range(x, N):
            print_seq([*seq, arr[i]], i, cnt+1)

# N, M 입력
N, M = map(int, sys.stdin.readline().strip().split())

# N개의 수 입력
arr = sorted(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    print_seq([arr[i]], i, 1)