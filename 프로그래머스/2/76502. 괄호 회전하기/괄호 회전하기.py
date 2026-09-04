# 1 <= n <= 1,000
def solution(s):
    answer = 0
    n = len(s)
    
    pairs = {')': '(', ']': '[', '}': '{'}
    arr = s + s
    for i in range(n): # i는 시작 위치
        stack = []
        # i 부터 i + n까지
        flag = True
        for j in range(i, i+n):
            if arr[j] in ')]}': # 닫는 괄호일때
                # stack에 여는 괄호 짝이 있어야 함
                if stack and pairs[arr[j]] == stack[-1]:
                    stack.pop()
                else:
                    flag = False
                    break
            else:
                stack.append(arr[j])
        
        if flag and not stack:
            answer += 1
    return answer

'''
괄호로 이루어진 문자열 s가 주어짐
s를 왼쪽으로 x칸 만큼 회전시켰을때
s가 올바른 괄호 문자열이 되게하는 x의 개수를 return
----------------------------------------------
문자열 s 2개를 연결
고정길이 n만큼 이동하며 검사

----------------------------------------------
1000 x 1000

'''