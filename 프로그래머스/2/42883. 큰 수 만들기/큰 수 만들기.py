# 2 <= len(number) <= 1,000,000
# 1 <= k < len(number)
def solution(number, k):
    stack = []
    
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)
    
'''
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24]를 만들 수 있다
가장 큰 숫자는 94이다

-----------------------------------------------------
1. 모든 number의 원소를 방문
2. 이전 숫자가 현재 숫자보다 작다면 제거
3. 
'''