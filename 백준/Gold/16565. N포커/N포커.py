import sys
input = sys.stdin.readline

# 첫째 줄에 N장의 카드를 뽑았을 때, 플레이어가 *이기는* 경우의 수를 10,007로 나눈 나머지를 출력

# 뽑는 카드의 수 N (1 <= N <= 52)
N = int(input().strip())

mod = 10_007
from math import comb

# 포함 배제의 원리
ans = 0
for i in range(1, N//4+1):
    if i % 2:
        ans = ans + (comb(13, i)*comb(52-4*i, N-4*i)) % mod
    else:
        ans = ans - (comb(13, i)*comb(52-4*i, N-4*i)) % mod

print(ans % mod)

"""
52장의 카드에서 N장의 카드를 뽑음
뽑은 카드들로 포카드 족보를 만들 수 있다면 플레이어의 승리, 아니라면 딜러의 승리
포카드란 뽑은 N장의 카드 중 같은 숫자 and 다른 문양인 4장의 카드"
"""