import sys
input = sys.stdin.readline

def solve():
    # N 수열의 길이 (1 <= N <= 1,000)
    N = int(input().strip())

    # A (1 <= A[i] <= 1,000)
    A = list(map(int, input().strip().split()))

    ans = []
    for i in range(N):
        if not ans or ans[-1] > A[i]:
            ans.append(A[i])
        
        else:
            l, r = 0, len(ans)
            while l < r:
                m = (l + r) // 2

                if ans[m] > A[i]: l = m+1
                else: r = m
            ans[l] = A[i]
    
    print(len(ans))

if __name__ == '__main__':
    solve()

"""
수열 A가 주어졌을 때 가장 긴 감소하는 부분 수열을 구해라

"""