import sys
input = sys.stdin.readline

import time
# A[0 ~ n] 에서 4개의 원소만 꺼냈을 때 합이 w가 되는 부분집합이 존재하면 YES, 없으면 NO

# 무게 w (10 <= w <= 799,994); 원소 개수 n (4 <= n <= 5,000)
w, n = map(int, input().strip().split())

# A 입력 (1 <= A[i] <= 200,000) 각 물품의 무게는 모두 다름
A = sorted(list(map(int, input().strip().split())))

s = [0]*(w+1) # 두 물품의 합 < w
def solve():
    for i in range(n):
        for j in range(i):
            # 두 수의 합이 w 보다 작은 경우만
            SUM = A[i]+A[j]
            if w <= SUM: break
            s[SUM] = (j, i)

    for i in range(n):
        for j in range(i):
            SUM = A[i] + A[j]
            if w <= SUM: break
            if s[w-SUM] and i not in s[w-SUM] and j not in s[w-SUM]:
                return 'YES'

    return 'NO'

print(solve())
