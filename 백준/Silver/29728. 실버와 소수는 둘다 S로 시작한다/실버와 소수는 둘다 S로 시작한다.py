import sys
input = sys.stdin.readline

"""
문자열 A에 포함된 알파벳 B의 개수, S의 개수를 공백으로 구분해 출력

- 빈 문자열 A를 준비
- N의 정수를 불렀을 때 다음 작업을 진행
    1. 현재 차례가 소수 번째가 아닌 경우: A의 끝에 B 추가
    2. 소수 번째인 경우: A의 마지막 문자가 B인 경우 마지막 문자를 S로 교체, A의 끝에 S를 추가
        B가 아닌 경우 끝에 S하나 추가 후 A를 뒤집는다
"""
# 정수 N (1 <= N <= 5,000,000)
N = int(input().strip())

# 우선 N의 범위에 존재하는 모든 소수를 찾아냄

P = ['B', 'B'] + ['S']*(N-1)
for i in range(2, int((N+1)**0.5) + 1):
    if P[i] == 'B': continue
    for j in range(i*2, N+1, i):
        if P[j] == 'B': continue
        P[j] = 'B'

cnt = {'B': 0, 'S': 0}

arr = P.copy()
for i in range(N, 0, -1):
    if P[i] == 'S':
        arr[i-1] = 'S'
    
    cnt[arr[i]] += 1

print(*cnt.values())

"""
[B, S]
1  [1, 0]
2  [0, 2]
3  [0, 3]
4  [1, 3]
5  [0, 5]
6  [1, 5]
7  [0, 7]
8  [1, 7]
9  [2, 7]
10 [3, 7]
11 [2, 9]
12 [3, 9]
13 [2, 11]

소수의 이전 숫자가
"""