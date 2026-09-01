from collections import Counter
# 2 <= n <= 100,000
# 100 <= weights[i] <= 1,000
def solution(weights):
    answer = 0
    n = len(weights)
    
    count = Counter(weights)
    for i in range(100, 1001): # 1:1, 2:3, 2:4, 3:4 인 경우를 구함
        answer += count[i] * (count[i]-1) / 2
        answer += count[i] * count[i * 3 / 2]
        answer += count[i] * count[i * 2]
        answer += count[i] * count[i * 4 / 3]
    
    return answer

'''
시소는 중심으로부터 2, 3, 4 거리의 지점에 좌석이 하나씩 있다

탑승자의 무게와 시소 축과 좌석 간의 거리곱이 같다면 시소 짝꿍

무게가 주어질때, 시소 짝꿍이 몇 쌍 존재하는지 구해라

----------------------------------------------------------


'''