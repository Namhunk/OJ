import sys
input = sys.stdin.readline

from itertools import permutations
import copy
def solve():
    # 3 <= N, M <= 50, 1 <= K <= 6
    N, M, K = map(int, input().strip().split())

    A = []
    for _ in range(N):
        A.append(list(map(int, input().strip().split())))
    
    R = []
    for _ in range(K):
        R.append(tuple(map(int, input().strip().split())))
    
    ans = float('inf')
    for seq in permutations(R, len(R)):
        temp = copy.deepcopy(A)
        SUM = 0
        for r, c, s in seq:
            rotate(temp, r-1, c-1, s)
        
        for i in range(N):
            ans = min(ans, sum(temp[i]))

    return ans

def rotate(arr, r, c, s):
    for layer in range(1, s+1):
        top, left = r - layer, c - layer
        bottom, right = r + layer, c + layer

        prev = arr[top][left]
        # 위쪽
        for j in range(left+1, right+1):
            arr[top][j], prev = prev, arr[top][j]
        # 오른쪽
        for i in range(top+1, bottom+1):
            arr[i][right], prev = prev, arr[i][right]
        # 아래쪽
        for j in range(right-1, left-1, -1):
            arr[bottom][j], prev = prev, arr[bottom][j]
        # 왼쪽
        for i in range(bottom-1, top-1, -1):
            arr[i][left], prev = prev, arr[i][left]
  
if __name__ == '__main__':
    print(solve())

"""
N x M 크기 배열, 회전 연산이 주어짐

각 회전을 한번씩 모두 수행했을 때 배열 A의 최솟값

r, c, s 로 연산되는 사각형은 정사각형의 크기를 가짐

정사각형의 크기가 최소 2일때 회전을 수행

모든 연산을 완료한 뒤 얻는 A의 최솟값

1. 회전의 범위는 (r-s, c-s) -> (r+s, c+s)


"""