from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

sn, bn = 0, 10**9
visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]
while sn <= bn:
    mn = (sn+bn)//2
    if arr[0][0] <= mn:
        visited[0][0][1] = mn
        que = deque([(0, 0, 1)])

        while que:
            x, y, cnt = que.popleft()
            for r, c in move:
                if cnt:
                    if 0 <= x+r*2 < n and 0 <= y+c*2 < m and visited[x+r*2][y+c*2][cnt-1] != mn and arr[x+r*2][y+c*2] <= mn:
                        visited[x+r*2][y+c*2][cnt-1] = mn
                        que.append((x+r*2, y+c*2, cnt-1))
                
                if 0 <= x+r < n and 0 <= y+c < m and visited[x+r][y+c][cnt] != mn and arr[x+r][y+c] <= mn:
                    visited[x+r][y+c][cnt] = mn
                    que.append((x+r, y+c, cnt))
        
        if min(visited[n-1][m-1]) != mn: sn = mn+1
        else: bn = mn-1
    
    
    else:
        sn = mn+1

print(sn)