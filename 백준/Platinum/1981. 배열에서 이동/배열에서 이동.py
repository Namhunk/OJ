from collections import deque
import sys

n = int(sys.stdin.readline().strip())
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arr = []
num_list = set()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in arr[i]:
        num_list.add(j)

num_list = sorted(list(num_list))
visited = [[-1]*n for _ in range(n)]
visited_num = 0

def solv():
    low = high = 0
    ans = float('inf')

    while low < len(num_list) and high < len(num_list):
        if bfs(num_list[low], num_list[high]):
            if low == high:
                return 0
            else:
                ans = min(ans, abs(num_list[high] - num_list[low]))
                low += 1
        
        else: high += 1
    
    return ans

def bfs(low, high):
    global visited, visited_num
    if arr[0][0] < low or arr[0][0] > high:
        return False
    
    visited_num += 1
    visited[0][0] = visited_num
    que = deque([(0, 0)])

    while que:
        x, y = que.popleft()
        if (x, y) == (n-1, n-1): return True

        for r, c in move:
            if 0 <= x+r < n and 0 <= y+c < n and visited[x+r][y+c] != visited_num:
                if low <= arr[x+r][y+c] <= high:
                    visited[x+r][y+c] = visited_num
                    que.append((x+r, y+c))
    
    return False

print(solv())