# 1 <= target <= 100,000
import sys
from heapq import heappush, heappop
INF = sys.maxsize
def solution(target):
    answer = [INF, INF]
    
    dp = [[INF, 0] for _ in range(target + 1)]
    dp[0] = [0, 0]
    
    scores = []
    for i in range(1, 21):
        scores.append((i, 1))  # (점수, 싱글/불 여부)
    scores.append((50, 1))
    
    for i in range(1, 21):
        scores.append((i * 2, 0))
    
    for i in range(1, 21):
        scores.append((i * 3, 0))
    
    for i in range(1, target + 1):
        for score, is_single in scores:
            if i >= score:
                new_cnt = dp[i - score][0] + 1
                new_sb = dp[i - score][1] + is_single
                
                # 다트 수가 더 적거나, 같으면 싱글/불이 더 많은 경우 갱신
                if new_cnt < dp[i][0] or (new_cnt == dp[i][0] and new_sb > dp[i][1]):
                    dp[i] = [new_cnt, new_sb]
    
    return dp[target]
    
    


"""
목표점수 target이 주어졌을 때
최선의 경우 던질 다트 수와 그 때의 싱글 또는 불을 맞춘 횟수(합)을 순서대로 return

----------------------------------------

각 1부터 20까지의 숫자에 싱글, 더블, 트리플이 있음
정 중앙은 불(+50)

최소한의 다트로 0점을 만들고, 그 방법 중 싱글, 불을 최대한 많이 던지는 방법

큰 숫자부터 처리하면 가장 최소의 던지기 횟수가 나옴

"""