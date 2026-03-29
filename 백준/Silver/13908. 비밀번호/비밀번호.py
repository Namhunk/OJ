import sys
input = sys.stdin.readline

from math import comb
def solve():
    global seq
    # n(1 <= N <= 7), m(0 <= m <= n)
    n, m = map(int, input().strip().split())

    if m != 0:
        arr = list(map(int, input().strip().split()))
    else:
        arr = []
    
    ans = 0
    for i in range(m+1):
        ans += (-1)**i * comb(m, i) * (10-i)**n
    
    print(ans)
    
if __name__ == '__main__':
    solve()

"""
비밀번호의 길이, 일부 숫자가 주어질 때 모든 가능한 비밀번호 개수를 출력

n: 비밀번호 길이
m: 비밀번호에 들어가는 수의 개수

10^n: 중복을 포함한 모든 숫자의 순열
M:    필수로 포함해야 되는 숫자들의 집합(M은 중복 x)
m:    M 집합의 크기
k:    집합 M에서 몇 개의 숫자를 제외할 것인지

(10-k)^n : K개의 숫자를 제외했을때 만들수 있는 순열

모든 순열에서 k개의 숫자를 뽑아 순열로 만든 경우를 제외한다면
(i = 0, 1, 2, 3, .. m) (-1)^i x mCk x (10-k)^n

mCk:     m개의 숫자들 중 k개를 추출
(10-k)^n: 이때 남은 숫자들로 중복 순열을 구성
(-1)^k:   각 순열의 중복을 제거

ans = 0
for k in range(len(M))
    ans += (-1)^k x mCk x (10-k)^n

"""