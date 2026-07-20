from collections import deque
def solution(begin, target, words):
    n = len(words)
    answer = 0
    visit = [False]*n # 각 단어 사용 여부 배열
    if target not in words: # words에 target이 없는 경우 0
        return 0
    
    q = deque([(begin, 0)])
    while q:
        curr, cnt = q.popleft() # 현재 단어
        if curr == target:
            return cnt
        
        for i in range(n): # 모든 단어 확인
            if visit[i]: # 이미 사용한 단어라면 건너뜀
                continue
            
            diff = 0
            for j in range(len(curr)):
                if curr[j] != words[i][j]:
                    diff += 1
            
            if diff == 1:
                visit[i] = True
                q.append((words[i], cnt+1))
            

'''
begin -> target이 되기위한 최소 변환 횟수

1. begin -> target으로 되기 위해서는 words에 target 단어가 있어야 함
2. 퍼지듯이 변경 BFS

'''