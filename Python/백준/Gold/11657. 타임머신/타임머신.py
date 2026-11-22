import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = [float('inf')] * (N+1)
edges = []

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    edges.append((A, B, C))

def bellman_ford(start):
    arr[start] = 0

    for i in range(N):
        for j in range(M):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]

            if arr[cur_node] != float('inf') and arr[next_node] > arr[cur_node] + edge_cost:
                arr[next_node] = arr[cur_node] + edge_cost
                if i == N-1: return True
        
    return False

if bellman_ford(1): print(-1)
else:
    for i in range(2, N+1):
        if arr[i] == float('inf'):
            print(-1)
        else:
            print(arr[i])