# 1 <= n <= 100
# 1 <= len(results) <= 4,500
def solution(n, results):
    rank = [[0]*(n+1) for _ in range(n+1)]
    for a, b in results:
        rank[a][b] = 1
        rank[b][a] = -1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            if i == k: continue
            
            for j in range(1, n+1):
                if i == j or k == j: continue
                
                if rank[i][k] > 0 and rank[k][j] > 0:
                    rank[i][j] = 1
                    rank[j][i] = -1
                
                if rank[i][k] < 0 and rank[k][j] < 0:
                    rank[i][j] = -1
                    rank[j][i] = 1
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if i == j: continue
            if rank[i][j] != 0:
                cnt += 1
        
        if cnt == n-1:
            answer += 1
    
    return answer

"""
r
"""
