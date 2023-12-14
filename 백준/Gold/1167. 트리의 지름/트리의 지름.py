import sys

def dfs(x, d):
    global ans
    
    s = 0
    for nx, nd in arr[x]:
        if visited[nx]:
            visited[nx] = False
            result = dfs(nx, nd+d)+nd
            
            ans = max(ans, result+s)
            s = max(s, result)
            visited[nx] = True
    
    return s

V = int(sys.stdin.readline().strip())
arr = [[] for _ in range(V+1)]

for _ in range(V):
    input_ = list(map(int, sys.stdin.readline().strip().split()))
    
    for i in range(1, len(input_)-1, 2):
        arr[input_[0]].append((input_[i], input_[i+1]))

visited = [True]*(V+1)
visited[1] = False
ans = 0
dfs(1, 0)
print(ans)