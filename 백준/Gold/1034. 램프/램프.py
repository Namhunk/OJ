import sys
input = sys.stdin.readline

# 스위치를 K번 누른 후에 켜져있는 행의 최대값을 구해라

# 1 <= N, M <= 50
N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
K = int(input().strip())

cnt = [0]*N
if K % 2 == 1: # 횟수가 홀수일 때 행의 0의 개수가 홀수개 이고 K보다 작을 때
    for i in range(N):
        zero = arr[i].count(0) # 현재 행의 0의 개수
        if zero % 2 and zero <= K:
            for j in range(N):
                if arr[i] == arr[j]: # 현재 행과 비슷한 행에대해
                    cnt[i] += 1

else: # 횟수가 짝수일 때 행의 0의 개수가 짝수개 이고 K보다 작을 때
    for i in range(N):
        zero = arr[i].count(0) # 현재 행의 0의 개수
        if not zero % 2 and zero <= K:
            for j in range(N):
                if arr[i] == arr[j]:
                    cnt[i] += 1

print(max(cnt))