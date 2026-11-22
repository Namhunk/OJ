import sys
input = sys.stdin.readline

def solution():
    # 1 <= N <= 2 x 10^5, 1 <= D <= 10^9
    N, D = map(int, input().strip().split())
    A = []
    B = []
    ans = 0
    for i in range(N):
        t, a, b = map(int, input().strip().split())
        if t <= D:
            ans = max(ans, a+b)
        A.append([t, a])
        B.append([t, b])

    
    # 시간순 정렬
    A.sort(key=lambda x: x[0])
    B.sort(key=lambda x: x[0])

    for i in range(1, N):
        A[i][1] = max(A[i-1][1], A[i][1])
        B[i][1] = max(B[i-1][1], B[i][1])

    for i in range(N):
        l, r = 0, N
        while l < r:
            m = (l + r) // 2
            if A[i][0] + B[m][0] <= D:
                l = m+1
            else:
                r = m
        
        if A[i][0] + B[l-1][0] > D: continue
        if A[i][1] + B[l-1][1] > ans:
            ans = A[i][1] + B[l-1][1]
    print(ans)
        
if __name__ == '__main__':
    solution()

"""
요리는 동시에 불가능

처음에 A+B가 가장 큰 값을 정답으로 임시 저장

A_T + B_T <= D 인 경우에
A 점수가 큰 것 중 하나
B 점수가 큰 것 중 하나
"""