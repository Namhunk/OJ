import sys
input = sys.stdin.readline

# 첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱 ㄴㄴ 수의 개수를 출력

# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때,  그 수를 제곱 ㄴㄴ 수라고 한다. 제곱수는 정수의 제곱이다.
# min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱 ㄴㄴ 수가 몇 개 있는지 출력한다.

# 첫째 줄에 두 정수 min, max가 주어진다
# (1 <= min <= 1,000,000,000,000)
# (min <= max <= min + 1,000,000)

from math import ceil

MIN, MAX = map(int, input().strip().split()) # 최소, 최대
ans = [1] * (MAX-MIN+1) # 배열이 총 길이 최대값 - 최소값 + 1

square = [i**2 for i in range(2, int(MAX**0.5)+1)] # 제곱수의 최대값은 MAX 이하의 값
for i in square:
    idx = (ceil(MIN/i) * i) - MIN # 배열에서 제곱수로 나눠지는 값들 중 가장 작은 값의 위치

    while idx <= MAX-MIN: # 위치가 배열의 길이보다 작은 동안
        ans[idx] = 0 # 현재 위치에 0
        idx += i # 현재 위치에 제곱수를 더한 위치


print(sum(ans))
"""
1. 계산을 할 때 제곱수의 최대 값은 MAX값 이하의 값이어야 함
"""