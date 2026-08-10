from itertools import combinations
def solution(n, q, ans):
    answer = 0
    m = len(q)
    
    for c in combinations(range(1, n+1), 5):
        curr = set(c) # 현재 조합을 집합으로
        flag = 1
        for i in range(m):
            check = set(q[i])
            
            if len(curr & check) != ans[i]:
                flag = 0
                break
        
        if flag:
            answer += 1
    return answer

'''
비밀 코드로 가능한 정수 조합 개수

1 ~ n까지 서로 다른 정수 5개 오름차순
분석 도구는 m번

-------------------------------------
1. 랜덤으로 5개의 숫자를 뽑음
2. 뽑은 숫자들이 m개의 조건을 만족하면 통과


'''