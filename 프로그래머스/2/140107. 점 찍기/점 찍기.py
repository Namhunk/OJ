# 1 <= k <= 1,000,000
# 1 <= d <= 1,000,000
def solution(k, d):
    answer = 0
    R = d//k
    d2 = d**2
    
    for a in range(R+1):
        x2 = (a*k)**2
        
        if x2 > d2: break
        
        l, r = 0, R+1
        while l < r:
            m = (l + r) // 2
            y2 = (m*k)**2
            
            if x2 + y2 <= d2:
                l = m + 1
            else:
                r = m
        

        answer += l
    
    return answer
        
"""
(0, 0)으로 부터
x축 방향 a*k
y축 방향 b*k
만큼 떨어진 위치에 점을 찍음
원점과의 거리가 d를 넘는 위치에는 점을 찍지 않는다.

k, d = 2, 4 일때

(a*k, b*k) -> (0, 0), (0, 2), (0, 4), (2, 0), (4, 0), (2, 2)

시간 단축을 위해 이분탐색 적용
"""