def solution(s):
    global n
    n = len(s)
    answer = 1
    
    for i in range(n):
        odd = expand(i, i, s)
        even = expand(i, i+1, s)
        
        answer = max(answer, odd, even)
    return answer

def expand(left, right, s):
    while left >= 0 and right < n and s[left] == s[right]:
        left -= 1
        right += 1
        
    return right - left - 1
'''
문자열이 주어짐 최대 2,500
부분 문자열 중 가장 긴 펠린드롬의 길이

정답의 최소 길이는 1 
abaaba
'''