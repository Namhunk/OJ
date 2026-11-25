import sys
import random, math
input = sys.stdin.readline

    
def solve():
    pass

def main():
    # 1 <= N <= 50
    N = int(input().strip())

    # 각 사람들이 친구로 생각하는 경우를 써놓음
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        rows = list(input().strip())
        for j in range(N):
            if rows[j] == 'N': continue
            arr[i][j] = 1

    ans = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N): # 1 : 1로 친구라고 생각하는 경우
            if arr[i][j] == 1 and arr[j][i] == 1:
                ans[i][j] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j: continue
                if arr[i][k] == arr[k][i] == 1 and arr[j][k] == arr[k][j] == 1:
                    ans[i][j] = 1

    ret = 0
    for i in ans:
        ret = max(ret, i.count(1))

    print(ret)
if __name__ == '__main__':
    main()  

"""
A가 B의 2-친구가 되려면, (A, B)이거나 (A, C), (B, C) 이어야 함

예제 3

0 1 0 0 0
1 0 1 0 0
0 1 0 1 0
0 0 1 0 1
0 0 0 1 0


"""