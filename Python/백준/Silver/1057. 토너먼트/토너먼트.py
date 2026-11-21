import sys
from math import ceil
input = sys.stdin.readline

# N = 참가자 수, J = 김지민 번호, H = 임한수 번호
# (2 <= N <= 100,000, J, H <= N)
N, J, H = map(int, input().strip().split())


R = 1

while ceil(J / (2**R)) != ceil(H / (2**R)):
	R += 1

print(R)
"""
N명의 참가자는 1부터 N까지 숫자를 배정 받음
인접한 번호끼리 붙음

참가자 수 가 홀수라면 마지막 번호는 부전승

J, H 가 서로 만날때까지 이긴다고 할 때
둘은 몇 라운드에서 만날지

1, 2 = 1
3, 4 = 2
5, 6 = 3
7, 8 = 4
9, 10 = 5

다음 라운드가 시작될때 참가자들은 자신의 숫자에 1/2를 곱한 숫자로 결정됨

"""