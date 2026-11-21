import sys
input = sys.stdin.readline

def solve(N, K, T, A):
	A.sort() # 바구니 오름차순 정렬
	
	arr = [0]*(N+1) # 나도리를 누적 배열
	total = 0 # 전체 나도리 개수
	
	for i in range(N):
		total += A[i]
		arr[i+1] = arr[i]+A[i]
	
	if total == 0:
		return "YES"

	if total < K or total % K != 0: # 전체 나도리 합이 K보다 작거나 정확히 K개가 아닌경우
		return "NO"
	
	# 나도리를 모두 옮겼을때 total // K개의 바구니만 남음
	p = total // K
	
	# 그때의 나도리 이동횟수
	if arr[N-p] <= T:
		return "YES"
	else:
		return "NO"
	

# (2 <= N, K <= 10^5, 0 <= T <= 10^9)
N, K, T = map(int, input().strip().split())

# (0 <= A[i] < K)
A = list(map(int, input().strip().split()))

print(solve(N, K, T, A))


"""
나도리 K 마리가 한 바구니에 모이면 터짐

N개의 바구니가 있고, i번째 바구니에는 A[i] 마리 담김
한 바구니에 있는 나도리 한 마리를 다른 바구니로 옮긴는 행동을 최대 T회 반복해
모든 나도리를 터트릴 수 있는지 알고 싶다

나도리는 한마리씩만 옮기는것이 가능

T회 이하로 나도리를 옮겨 모두 터트리는것이 가능하면 YES 불가능하면 NO 출력
------------------

1. 바구니의 전체 숫자 합이 K보다 작거나, K로 나누어 떨어지지 않는다면 불가능
	- 전체 나도리의 개수를 구함

2. T회 이하로 수행해야함
	-1. 나도리 배열을 오름차순 정렬

"""