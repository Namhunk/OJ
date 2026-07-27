def solution(sticker):
    n = len(sticker)
    answer = 0
    
    if n == 1:
        return sticker[0]
    
    answer = max(answer, find_answer(n, 0, sticker))
    answer = max(answer, find_answer(n, 1, sticker))
        
    return answer

def find_answer(n, start, arr):
    dp = [0]*n
    for i in range(1, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[start+i-1])
    
    return dp[-1]
'''
원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티케에 적힌 숫자 합이 최대가 되도록
한 장을 뜯으면 양옆 스티커는 사용불가

[14, 6, 5, 11, 3, 9, 2, 10]

n개의 원소가 있다 할 때
1. 0 ~ n-2까지
2. 1, n-1까지
[0, 14, 6, 5, 11, 3, 9, 2, 10]
'''