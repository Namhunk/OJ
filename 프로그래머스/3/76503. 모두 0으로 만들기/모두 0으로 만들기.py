import sys

sys.setrecursionlimit(10**6)
def solution(a, edges):
    global graph, visit, answer
    answer = 0
    
    if sum(a) != 0:
        return -1
    
    n = len(a)
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visit = [False]*(n+1)
    visit[0] = True
    
    dfs(0, a)
    return answer

def dfs(x, a):
    global answer
    for nx in graph[x]:
        if visit[nx]: continue
        
        visit[nx] = True
        child = dfs(nx, a)
        answer += abs(child)
        a[x] += child
    
    return a[x]
        