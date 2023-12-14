from collections import deque
import sys

while True:
    Input = sys.stdin.readline().strip()
    if len(Input) > 0: l, r, c = map(int, Input.split())
    else: continue
    if not l and not r and not c: break

    arr = []
    while len(arr) < l:
        f = []
        while len(f) < r:
            t = list(" ".join(sys.stdin.readline().strip()).split())
            if len(t) > 0:
                f.append(t)
        
        arr.append(f)
    
    visited = [[[True] * c for _ in range(r)] for _ in range(l)]
    time = [[[-1] * c for _ in range(r)] for _ in range(l)]
    que = deque()
    for x in range(l):
        for y in range(r):
            for z in range(c):
                if arr[x][y][z] == '#':
                    visited[x][y][z] = False
                
                if arr[x][y][z] == 'S':
                    visited[x][y][z] = False
                    que.append((x, y, z))
                    time[x][y][z] = 0
                
                if arr[x][y][z] == 'E':
                    E = (x, y, z)

    while que:
        x, y, z = que.popleft()
        for k in range(-1, 2, 2):
            if 0 <= x+k < l and visited[x+k][y][z]:
                visited[x+k][y][z] = False
                time[x+k][y][z] = time[x][y][z] + 1
                que.append((x+k, y, z))
            
            if 0 <= y+k < r and visited[x][y+k][z]:
                visited[x][y+k][z] = False
                time[x][y+k][z] = time[x][y][z] + 1
                que.append((x, y+k, z))
            
            if 0 <= z+k < c and visited[x][y][z+k]:
                visited[x][y][z+k] = False
                time[x][y][z+k] = time[x][y][z] + 1
                que.append((x, y, z+k))
    
    print(f"Escaped in {time[E[0]][E[1]][E[2]]} minute(s)." if time[E[0]][E[1]][E[2]] >= 0 else "Trapped!")