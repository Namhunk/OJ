def solution(sticker):
    answer = 0
    N = len(sticker)
    if N > 2:
        answer = max(answer, get_sticker(N, sticker[:N-1]))
        answer = max(answer, get_sticker(N, sticker[1:]))
    else:
        answer = max(sticker)
    return answer

def get_sticker(N, arr): # s, e = 시작, 종료 위치, arr = sticker배열
    DP = [0] * N # 배열의 전체 크기는 N
    
    for i in range(1, N): # 첫 값을 아무것도 없는 0으로, 1부터 arr[0]을 챙김
        if i == 1: DP[i] = arr[i-1]
        
        DP[i] = max(DP[i-1], DP[i-2]+arr[i-1])

    return DP[-1]
    
'''
스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return
스티커 한장을 뜯으면 양 옆을 못씀

1. 0부터 시작한다면 N-1까지만 가능
2. 1부터 시작한다면 N 까지 가능
3. 각 값들에 대해 DP 수행

'''