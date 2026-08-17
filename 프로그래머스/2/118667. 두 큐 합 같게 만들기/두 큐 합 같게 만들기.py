
def solution(queue1, queue2):
    answer = -1
    
    total = sum(queue1) + sum(queue2)
    if total % 2 == 1:
        return answer
    
    target = total // 2
    n = len(queue1)
    
    arr = queue1 + queue2 + queue1 + queue2
    
    curr = sum(queue1)
    cnt = 0
    
    l, r = 0, n-1
    while curr != target:
        if cnt > 4*n:
            return -1
        
        if curr < target:
            r += 1
            curr += arr[r]
        else:
            curr -= arr[l]
            l += 1
        
        cnt += 1
    
    answer = cnt
    return answer

'''

'''