import sys
input = sys.stdin.readline
# N x M 직사각형
# 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾아라

ans = 1 # 정답

# N, M 입력(1 <= N, M <= 50)
N, M = map(int, input().strip().split())

arr = [list(map(int, input().strip())) for _ in range(N)]

K = min(N, M) # 둘 중 작은것
for k in range(K-1, 0, -1): # 1은 제외 결국 2에서 안나오면 답은 1
	for i in range(N-k):
		for j in range(M-k):
			if arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]:
				ans = max(ans, (k+1)**2)

print(ans)
	
"""
가장 작은 정사각형은 1

현재 i 번째 행에서 발견한 두 위치의 거리가 k 일때
두 위치의 +k 또는 -k의 위치에 같은 숫자가 존재 해야함

행을 기준으로 검사 할 때
열은 K
"""