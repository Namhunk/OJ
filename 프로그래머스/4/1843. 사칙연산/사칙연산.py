# len(arr) % 2 == 1
INF = 10**15
def solution(arr):
    nums = []
    ops = []
    
    for i, x in enumerate(arr):
        if i % 2 == 0:
            nums.append(int(x))
        else:
            ops.append(x)
    
    n = len(nums)
    maxDP = [[-INF]*n for _ in range(n)]
    minDP = [[INF]*n for _ in range(n)]
    
    for i in range(n):
        maxDP[i][i] = nums[i]
        minDP[i][i] = nums[i]
    
    for l in range(2, n+1):
        for i in range(0, n-l+1):
            j = i + l - 1
            
            for k in range(i, j):
                op = ops[k]
                
                if op == '+':
                    cand_max = maxDP[i][k] + maxDP[k+1][j]
                    cand_min = minDP[i][k] + minDP[k+1][j]
                else:
                    cand_max = maxDP[i][k] - minDP[k+1][j]
                    cand_min = minDP[i][k] - maxDP[k+1][j]
                
                if cand_max > maxDP[i][j]:
                    maxDP[i][j] = cand_max
                    
                if cand_min < minDP[i][j]:
                    minDP[i][j] = cand_min
                    
    answer = maxDP[0][n-1]
    return answer

"""
문자열 형태의 숫자, (+, -)가 주어질 때

서로 다른 연산순서의 계산 결과 중 최댓값

0   1  -3   5  -8
1   1   8   8  -3
2   
"""