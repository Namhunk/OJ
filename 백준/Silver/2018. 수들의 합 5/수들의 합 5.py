import sys
input = sys.stdin.readline

def solve():
    # N (1 <= N <= 10,000,000)
    N = int(input().strip())


    cnt = 0
    l = 0
    l_SUM = 0
    r_SUM = 0
    for r in range(N+1):
        r_SUM += r
        while r_SUM - l_SUM > N:
            l += 1
            l_SUM += l

        if r_SUM - l_SUM == N:
            cnt += 1
        
    print(cnt)

if __name__ == '__main__':
    solve()

"""

"""