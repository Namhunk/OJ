# 1 <= n <= 100
# 1 <= cards[i] <= 100
def solution(cards):
    answer = 0
    n = len(cards)
    
    scores = []        # 각 세트 개수
    visit = [False]*n  # 각 위치의 방문 표시
    
    for i in range(n): # 모든 숫자
        if visit[i]: continue # 방문하지 않은 경우만
        cnt = 1            # 방문 위치 개수
        visit[i] = True    # 현재 위치 방문처리
        stack = [cards[i]-1] # 다음 위치
        
        while stack:
            x = stack.pop()
            if visit[x]: continue
            cnt += 1
            visit[x] = True
            stack.append(cards[x]-1)
        
        scores.append(cnt)
    
    scores.append(0) # 1번만에 모든 숫자를 도는 경우를 고려
    scores.sort(reverse=True)
    answer = scores[0] * scores[1]

    return answer

'''
게임에서 얻을 수 있는 최고 점수를 구해라
1. cards 배열이 주어짐
2. 0 부터 cards 길이 이하의 idx를 하나 선택 
3. 해당 위치의 cards[idx]가 다음 이동할 next_idx
4. 이전에 방문한 idx에 도착한 경우 종료
5. 아직 방문하지 않은 다음 idx를 찾음
6. 3번, 4번, 5번 반복
7. 모든 위치의 방문이 끝나면 각 세트별 숫자 개수를 구함
8. 내림차순 정렬 후 앞에서 부터 2개의 값을 곱함

'''