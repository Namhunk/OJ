# 1 <= N <= 200,000,000
# 1 <= len(stations) <= 10,000
# 1 <= W <= 10,000

from math import ceil
def solution(n, stations, w):
    answer = 0
    stations.sort()
    
    coverage = 2*w + 1 # 전파 길이
    arr = []
    before = 1 # 시작 번호
    
    for x in stations:
        left = x - w
        right = x + w
        
        if left > before:
            dist = left - before
            arr.append(dist)

        before = right + 1
    
    if before <= n:
        dist = n - before + 1
        arr.append(dist)
    
    for dist in arr:
        answer += ceil(dist / coverage)
    
    return answer
        

'''
N개의 아파트
stations 의 기존 기지국
전파의 거리 W

모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국 개수 최솟값
----------------------------------------

기지국을 중심으로 총 2W+1 만큼의 길이가 전파 거리가 됨

1. 현재 기지국의 전파가 오지 않는 아파트을의 범위를 구함
2. 각 범위에서 최소 기지국 설치 개수를 구함
3. 모든 개수를 더함


'''