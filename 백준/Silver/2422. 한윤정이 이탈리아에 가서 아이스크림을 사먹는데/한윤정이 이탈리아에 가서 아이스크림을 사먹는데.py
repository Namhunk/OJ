import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().strip().split())
    ice = {i: set() for i in range(1, N+1)}
    for _ in range(M):
        a, b = sorted(map(int, input().strip().split())) # 작은수가 앞에 오도록
        ice[a].add(b)

    ans = 0
    arr = [i for i in range(N+1)] # 전체 숫자의 list
    for i in range(1, N-1):
        nums = set(arr[i+1:]) - ice[i] # ice[i]에 포함되지 않는 다음 숫자들
        if len(nums) > 1:
            for j in nums:
                temp = set(arr[j+1:]) - (ice[j]|ice[i])
                ans +=len(temp) # ice[j]에 포함되지 않는 다음 숫자들
    
    print(ans)

    

if __name__ == '__main__':
    solve()

"""
N개의 아이스크림이 있고 1 - N 까지 번호가 있음
같이 먹으면 맛없는 아이스크림이 있음
아이스크림 3가지를 선택하는 경우의 수

1. 1 - N-2 범위에서 아이스크림을 고름
2. i+1 - N
"""