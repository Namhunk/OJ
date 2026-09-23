# 3 <= len(elements) <= 1,000
# 1 <= elements[i] <= 1,000
def solution(elements):
    N = len(elements)
    answer = 0
    total = set()
    
    arr = elements*2 # 배열 길이 2배
    
    for l in range(1, N+1): # 길이
        for i in range(1, N+1): # 시작 위치
            total.add(sum(arr[i: i+l]))
            
    answer = len(total)
        
    return answer

'''
O(N^2)? 

1,000 x 1,000
'''
