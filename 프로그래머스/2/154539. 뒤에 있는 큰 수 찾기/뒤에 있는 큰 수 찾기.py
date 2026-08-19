# 4 <= n <= 1,000,000
def solution(numbers):
    n = len(numbers)
    answer = [-1]*n
    
    stack = []
    for i in range(n):
        while stack and stack[-1][0] < numbers[i]:
            _, idx = stack.pop()
            answer[idx] = numbers[i]
        
        stack.append((numbers[i], i))
    
    return answer

'''
각 원소들에 대해 자신보다 뒤의 있는 숫자 중 자신보다 크면서 가까이 있는 수를 뒷 큰수 라고함
-----------------------------------------------------
1. 각 원소들을 돌며 현재 원소 다음에 자신보다 큰 수가 있는지 확인
2. 뒤에 자신보다 큰 원소가 있기만 하면 됨

-----------------------------------------------------

'''
