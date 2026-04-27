# 0 <= a, b <= 10^9
# 1<= len(g) = len(s) = len(t) = len(w) = N <= 10^5
# 0 <= g[i], s[i] <= 10^9
# 1 <= w[i] <= 10^2
# 1 <= t[i] <= 10^5
# a <= sum(g)
# b <= sum(s)
def solution(a, b, g, s, w, t):
    N = len(g)
    
    A, B = 0, 0 # 현재 금, 은 kg
    l, r = 1, 10**15
    answer = 0
    while l < r:
        m = (l + r) // 2
        if transport(m, a, b, g, s, w, t, N):
            answer = m
            r = m
        else:
            l = m+1
            
    return answer

def transport(T, a, b, g, s, w, t, N): # T시간 내에 운반할 수 있는 a, b의 최대 크기
    # T 시간동안
    SUM_G = 0 # 모든 금의 개수
    SUM_S = 0 # 모든 은의 개수
    SUM_TOTAL = 0 # 모든 합
    for i in range(N):
        time = t[i]
        weight = w[i]
        
        # T시간동안 해당 트럭의 왕복 횟수
        cnt = T // (time*2)
        
        # 왕복 수행 후 남은 시간이 있는 경우 마지막 편도 가능
        if T % (time*2) >= time: 
            cnt += 1
        
        # 해당 트럭의 총 운반 무게
        max_move = cnt * weight
        
        # 금, 은 따로 or 둘다 합쳐서
        gold_move = min(g[i], max_move)
        silver_move = min(s[i], max_move)
        total_move = min(g[i] + s[i], max_move)

        SUM_G += gold_move
        SUM_S += silver_move
        SUM_TOTAL += total_move
        
    if SUM_G >= a and SUM_S >= b and SUM_TOTAL >= (a + b):
        return True
    
    return False
        

"""
새 도시를 짓기로 함

도시를 짓는 장소엔 금 a kg, 은 b kg 이 필요
각 도시에는 번호가 존재
i번 도시에는 금g[i], 은 s[i], 트럭 한 대가 있음

i번 도시 트럭은 새 도시와 i번 도시만을 왕복 가능
편도 t[i]시간, w[i] kg 운반 가능

금 a kg, 은 b kg을 전달할 수 있는 가장 빠른 시간

도시 i 에는 금 g[i], 은 s[i] 이 있고, w[i] 의 무게를 t[i] 시간만큼 이동시킴

배열의 길이는 최대 10^5

이분탐색으로 최대 시간이 T인 경우
가능한지 or 불가능한지 판단 후 T 시간 조정

"""