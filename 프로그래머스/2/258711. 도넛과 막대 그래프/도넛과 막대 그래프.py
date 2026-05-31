# 1 <= len(edges) <= 1,000,000
# 1 <= a, b <= 1,000,000
def solution(edges):
    global graph, visit
    answer = [0]*4 # 정답 배열
    MAX_SIZE = 1_000_001 # 최대 크기
    graph = {i: [] for i in range(MAX_SIZE)} # 그래프
    visit = [False]*(MAX_SIZE) # 방문 기록
    indegree = [0]*MAX_SIZE # 다른 노드에서 현재 노드로 올 수 있는지
    nodes = set()
    
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1
        nodes.add(a)
        nodes.add(b)
    
    s = [0, 0]
    for i in range(1, MAX_SIZE):
        if i not in nodes: continue
        if len(graph[i]) >= 2 and indegree[i] == 0: # 생성 정점은 최소 2개와 연결
            if len(graph[i]) > s[1]:
                s = [i, len(graph[i])]
    
    answer[0] = s[0]
    
    # 막대 그래프 부터
    for i in range(1, MAX_SIZE):
        if i not in nodes: continue
        if i == answer[0]: continue # 생성 정점은 건너뜀
        if indegree[i] != 0: continue
        if visit[i]: continue # 방문하지 않은 정점만

        visit[i] = True
        n, e = shape(i, 1, 0)
        answer[2] += 1
    
    for nx in graph[answer[0]]:
        if visit[nx]: continue
        visit[nx] = True
        n, e = shape(nx, 1, 0)
        
        if n == e:
            answer[1] += 1
        elif n-1 == e:
            answer[2] += 1
        else:
            answer[3] += 1
            
    return answer

from collections import deque
def shape(i, n, e):
    global visit
    q = deque([i])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            e += 1
            if visit[nx]:continue
            visit[nx] = True
            
            n += 1
            q.append(nx)
    
    return n, e
        
"""
그래프는 도넛모양, 막대모양, 8자 모양이 있음

return [정점 번호, 도넛 수, 막대 수, 8자 수]

1. 생성 정점은 받는 화살표가 없음
2. 정점의 개수, 간선의 개수 count
3. 사이클을 만들고 정점 n개, 간선 n개면 도넛
4. 사이클이 없고 정점 n개 간선 n-1개 면 막대
5. 사이클이 2개 있고 간선이 n+1개면 8자
6. 모든 그래프 개수의 합은 2이상

-----------------------------------------------

1. 생성 정점을 찾음
2. 생성 정점을 제외한 나머지 
"""