import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
coin = [int(input().strip()) for _ in range(n)]

# n개의 동전을 적당히 사용해 가치의 합이 k원이 되도록

# 경우의 수 출력
# 동전의 구성이 다른 경우만

# 동전은 최대 100개의 종류, 각 가치는 1 부터 100,000

# 동전의 최솟값이 1이라면 1의 합이 k가 되려면 k개 필요

arr = [0]*(k+1)
arr[0] = 1

for num in coin:
    for idx in range(num, k+1):
        arr[idx] = arr[idx] + arr[idx-num]

print(arr[k])