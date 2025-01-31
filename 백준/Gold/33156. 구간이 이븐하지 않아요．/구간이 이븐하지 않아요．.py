import sys
input = sys.stdin.readline


# 연속된 부분 수열 A[l,r]을 절반으로 나눠 얻은 두 수열이 서로 이븐할 때, A[l,r]의 최대 길이를 출력한다
# 만약 그러한 연속된 부분 수열이 존재하지 않는다면, 0을 출력한다

# 수열 A의 길이인 정수 N이 주어진다. (1 <= N <= 5,000)
N = int(input().strip())
A = list(map(int, input().strip().split()))

idx = {j: i for i, j in enumerate(sorted(set(A)))}
D = len(set(A))

arr = [[0]*(N+1) for _ in range(D)]
for i in range(N):
    arr[idx[A[i]]][i+1] = 1
    
for d in range(D):
    for i in range(1, N+1):
        arr[d][i] += arr[d][i-1]

start = N if N % 2 == 0 else N-1
for i in range(start, 1, -2):
    half = i // 2
    for l in range(N-i+1):
        r = l + i -1
        m = (l + half -1)
        flag = True

        for d in range(D):
            left = arr[d][m+1] - arr[d][l]
            right = arr[d][r+1] - arr[d][m+1]
            if left != right:
                flag = False
                break

        if flag:
            print(i)
            exit()

print(0)




"""
연속된 구간을 반으로 나눌때 각 구간들의 숫자들의 개수가 같은지

"""