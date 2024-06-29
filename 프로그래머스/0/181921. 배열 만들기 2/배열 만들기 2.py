from collections import deque

def solution(l, r):
    answer = []
    arr = []
    que = deque(['5'])
    while que:
        num = que.popleft()
        if l <= int(num) <= r: answer.append(int(num))
        
        if int(num+'0') <= r: que.append(num+'0')
        if int(num+'5') <= r: que.append(num+'5')
    
    if not len(answer): answer.append(-1)
    return answer