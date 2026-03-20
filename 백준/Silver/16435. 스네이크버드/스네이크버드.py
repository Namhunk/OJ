import sys
input = sys.stdin.readline

def solve():
    # 과일의 개수 N (1 <= N <= 1,000), 스네이크 버드의 초기 길이 L (1 <= L <= 10,000)
    N, L = map(int, input().strip().split())

    # (1 <= H[i] <= 10,000)
    H = sorted(list(map(int, input().strip().split())))

    ans = L
    for i in range(N):
        if H[i] > ans: break
        ans += 1
    
    print(ans)

if __name__ == '__main__':
    solve()

"""
스네이크 버드는 과일을 먹으면 길이가 1늘어난다
과일들은 지상으로 부터 높이 h를 두고 떨어져 있다
스네이크 버드는 자신의 길이보다 작거나 같은 높이에 있는 과일을 먹을 수 있다

"""