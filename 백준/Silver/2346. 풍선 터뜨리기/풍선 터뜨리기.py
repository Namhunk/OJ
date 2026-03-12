import sys
input = sys.stdin.readline

from collections import deque
def solve():
    # 자연수 N (1 <= N <= 1,000)
    N = int(input().strip())
    
    # 풍선 안의 종이에 적혀있는 수
    arr = list(map(int, input().strip().split()))
    q = deque()
    for i, val in enumerate(arr):
        q.append((i+1, val))

    ans = []
    while len(q) > 1:
        idx, val = q.popleft()
        ans.append(idx)

        if val >= 0:
            for _ in range(val-1):
                q.append(q.popleft())
        
        else:
            for _ in range(abs(val)):
                q.appendleft(q.pop())
    
    ans.append(q.popleft()[0])
    print(*ans)
        
if __name__ == '__main__':
    solve()

"""
처음에는 1번 풍선을 터뜨리고 그 종이에 나와있는 값 만큼 이동하여 다음 풍선을 터뜨린다
양수 -> 오른, 음수 -> 왼

"""