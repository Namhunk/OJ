def solution(n, m, x, y, queries):
    answer = -1
    
    # 행 이동, 열 이동을 각각 분리
    rows = []
    cols = []
    
    dirs = {0: -1, 1: 1, 2: -1, 3: 1}
    for d, dx in queries: # 방향에 따라 행, 열 이동 분리
        if d in (0, 1): # 열방향 이동
            cols.append(-dx*dirs[d])
        
        if d in (2, 3): # 행 방향 이동
            rows.append(-dx*dirs[d])
    
    answer = dist(n, x, rows)*dist(m, y, cols)
    return answer

def dist(N, start, arr):
    l, r = start, start # 이동했을때 범위를 구함
    for dx in arr[::-1]:
        new_l = 0 if l <= 0 <= r else l+dx
        new_r = N-1 if l <= N-1 <= r else r+dx
        
        l, r = max(0, new_l), min(N-1, new_r)
    
    print(l, r)
    if l > r:
        return 0
    else:
        return r-l+1
        
    
'''
l, r = 0, 0
1 1 1 1 1 -1




'''