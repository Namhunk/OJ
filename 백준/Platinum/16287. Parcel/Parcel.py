import sys
input = sys.stdin.readline

import time
# A[0 ~ n] 에서 4개의 원소만 꺼냈을 때 합이 w가 되는 부분집합이 존재하면 YES, 없으면 NO

# 무게 w (10 <= w <= 799,994); 원소 개수 n (4 <= n <= 5,000)
w, n = map(int, input().strip().split())

# A 입력 (1 <= A[i] <= 200,000) 각 물품의 무게는 모두 다름
A = sorted(list(map(int, input().strip().split())))

arr = [0]*(4*2*pow(10,5)+1)
for i in range(2, n-1):
    for j in range(i-1):
        arr[A[i-1]+A[j]] = 1

    for j in range(i+1, n):
        SUM = A[i] + A[j]
        if SUM >= w:
            break

        if arr[w-SUM]:
            print('YES')
            exit()

print('NO')