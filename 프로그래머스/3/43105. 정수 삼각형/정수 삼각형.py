def solution(triangle):
    N = len(triangle)
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = triangle[0][0]
    
    for i in range(N-1):
        for j in range(i+1):
            arr[i+1][j] = max(arr[i+1][j], arr[i][j] + triangle[i+1][j])
            arr[i+1][j+1] = max(arr[i+1][j+1], arr[i][j] + triangle[i+1][j+1]) 
    
    answer = max(arr[N-1])
    return answer

    
"""
삼각형의 정보가 담긴 triangle이 주어질 때, 거쳐간 숫자의 최댓값을 return

7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

0 -> 0, 1
1 -> 1, 2
2 -> 2, 3

"""