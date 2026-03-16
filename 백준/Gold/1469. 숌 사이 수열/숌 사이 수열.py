import sys
input = sys.stdin.readline

def solve():
    global N, X, ans
    # N(1 <= N <= 8)
    N = int(input().strip())

    # X[i](0 <= X[i] <= 16)
    X = sorted(list(map(int, input().strip().split())))
    ans = []
    create_S(0, (-1, )*2*N)
    
    if len(ans) == 0:
        print(-1)
    else:
        print(*sorted(ans)[0])

def create_S(idx, arr):
    arr = list(arr)
    if idx >= N: # N을 넘긴다는 것은 모든 숫자를 사용했다는 의미
        ans.append(arr)
    else:
        for i in range(2*N-X[idx]-1):
            l, r = i, i+X[idx]+1
            if arr[l] < 0 and arr[r] < 0:
                arr[l], arr[r] = X[idx], X[idx]
                create_S(idx+1, tuple(arr))
                arr[l], arr[r] = -1, -1
            

   
if __name__ == '__main__':
    solve()

"""
N개의 고유한 숫자로 구성되어있는 집합 X에서 각 숫자를 2번씩 사용해 2N 길이의 수열 S를 만들어라
1. X의 모든 숫자는 S에 2번 등장해야 함
2. X가 등장하는 수가 i라면, S에서 두 번 등장하는 i사이에는 수가 i개 등장해야 함

- 수열을 출력할 때 여러 개일 경우 사전순으로 가장 빠른 것을 출력
- 없는 경우 -1 출력
예를 들어
X = {1, 2, 3}
S = {2, 3, 1, 2, 1, 3}

X[i]의 크기가 작은 순서로 수행을 함
현재 위치 부터 X[i]+1 위치가 2N의 범위를 벗어나지 않고 해당 자리가 비어있다면 

6-4
0, 1
"""