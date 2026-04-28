# 1 <= len(works) <= 20,000
# 1 <= works[i] <= 50,000
# 1 <= n <= 1,000,000
import sys
INF = sys.maxsize
def solution(n, works):
    if sum(works) <= n:
        return 0
    works.sort() # 오름차순 정렬
    
    l, r = 0, max(works)
    while l < r: # n번 이하를 사용해 나올 수 있는 최댓값
        m = (l + r) // 2    
        cnt, _ = find(m, works)
        
        if cnt <= n:
            r = m
        else:
            l = m + 1
    
    k, s = find(l, works) # 최종 사용 횟수, l로 바꿀 시작 범위를 구함
    if s < len(works):
        n -= k
        works[s:] = [l]*(len(works) - s)
    
    length = len(works)
    i = 0
    while n > 0:
        idx = length - 1 - (i % length)   # 항상 0 ~ length-1 범위
        if works[idx] == 0:
            break                         # 더 이상 깎을 값이 없음
        works[idx] -= 1
        n -= 1
        i += 1
    
    answer = 0
    for i in range(len(works)): # 최종 값
        answer += works[i]**2
        
    return answer

def find(x, works): # works[i] 들 중 x보다 큰 값의 위치
    l, r = 0, len(works)
    while l < r:
        m = (l + r) // 2
        if works[m] <= x:
            l = m + 1
        else:
            r = m
    
    size = len(works) - l # 바꿀 원소의 개수
    ret = sum(works[l:]) - size*x
    
    return ret, l
    
    
        
            
    
"""
N시간 동안 야근 피로도를 최소화
1시간동안 작업량 1을 처리
야근을 시작한 시점에서 남은 일의 작업량을 제곱해 더한 값

1. 이분탐색 2개 사용
2. 첫 이분탐색은 n번 뺐을때 works의 최댓값
3. 
"""