def solution(land):
    answer = 0
    n = len(land)
    
    for i in range(1, n):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    
    answer = max(land[-1])
    return answer

'''
모든 땅은 n행 4열
각 행의 4칸 중 한 칸만 밟으면서 내려와야 함
내려올때 같은열을 계속해서 밟을 수 없음

---------------------------------------
1. 이전 다른 열에서 가장 큰 값

'''