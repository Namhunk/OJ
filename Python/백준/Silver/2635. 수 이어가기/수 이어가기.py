import sys
input = sys.stdin.readline

from math import ceil, floor
def solve():
    # N (1 <= N <= 30,000)
    A = int(input().strip())

    C = [0, 1, 1, 2]        # A에 곱할 계수들 저장
    left, right = 0, A      # B의 최소, 최대 범위
    left_B, right_B = 0, A  # 마지막 구간
    while left < right:
        # left, right 업데이트
        i = len(C)-1
        left_B, right_B = left, right
        left = ceil(C[i-1] * A // (C[i-2] + C[i-1])) # 최솟값은 유리수가 나오는 경우 ceil
        right = floor(C[i] * A // (C[i-1] + C[i])) # 최댓값은 유리수가 나오는 경우 floor

        # C 값 2개 추가, len(C) + 2
        for _ in range(2):
            C.append(C[-2] + C[-1])
    
    B = left_B
    best_len = -1
    for b in range(left_B, right_B+1):
        L = seq_len(A, b)
        if L > best_len:
            best_len = L
            B = b
    
    ans = [A, B]
    while ans[-2] >= ans[-1]:
        ans.append(ans[-2]-ans[-1])
    
    print(len(ans))
    print(*ans)

def seq_len(a, b):
    x, y = a, b
    cnt = 2
    while 1:
        z = x-y
        if z < 0: break
        cnt += 1
        x, y = y, z
    
    return cnt
            
if __name__ == '__main__':
    solve()

"""
1. 첫 번째 수로 양의 정수가 주어짐
2. 두 번째 수는 양의 정수 중 하나를 선택
3. 세 번째 이후로 나오는 모든 수는 n-2 위치에서 n-1 위치 수를 빼서 만듬
4. 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다

수열의 길이
각 값 출력

2번째 숫자를 선택하는데 가장 긴 수열을 만들게 숫자를 선택
-------------------------------------------------------

1. 첫 번째 숫자 A, 두 번째 숫자 B라고 했을 때
    4번째 숫자를 얻기 위해서는 A-B < B 이어야 함, 그래야 2B-A > 0, B > A/2(B는 A/2 보다 커야함)

2. 각 계산은 
    A, B, A-B, 2B-A, 2A-3B, 5B-3A, 5A-8B, 13B-8A, ... 의 형태
    모든 위치에서 값들이 0 이상이어야 함


3. (i >= 3) 일때
    각 A, B의 부호는 A: (-1)^(i+1), B: (-1)^i
    각 A, B의 계수는 A: 이전 B의 값, B: 이전 A계수 + B계수

4. 각 A, B의 계수만 봤을때
    i >= 2
    A = 0, 1, 1, 2, 3, 5, 8, 13, ...
    B = 1, 1, 2, 3, 5, 8, 13, 21, ...

5. C 라는 배열이 A에 대한 계수를 나타낸다면
    C[i] = C[i-2] + C[i-1]
    이때 i 위치에서의 A, B 계수는
    A = C[i], B = C[i-1] + C[i]

결국 전체 식은

C[i] = C[i-2] + C[i-1] 수행 후

(i -> ?)       (-1)^(i+1) x C[i] x A + (-1)^i x (C[i-1] + C[i]) x B >= 0

의 식

2번에 대한 추가적인 계산
A >= 0      |   0 <= A
B >= 0      |   0 <= B
A-B >= 0    |   B <= A
2B-A >= 0   |   A/2 <= B
2A-3B >= 0  |   B <= 2A/3
5B-3A >= 0  |   3A/5 <= B
5A-8B >= 0  |   B <= 5A/8
.
.
.

i = 3 인 경우 부터 계산하므로
0 <= B <= A 에 구간의 모든 값들을 사용해
현재 값이

조건의 범위를 만족하는지 검사

만약 현재 B가 구간의 조건을 만족한다면
다음 구간으로 좁혀줌

각 범위는

C = [0, 1, 1, 2, 3..]
C[i-1] x A / (C[i-2] + C[i-1]) <= B <= C[i] x A / (C[i-1] + C[i])

len(C) 최소 4 이상, 길이 2씩 증가
"""