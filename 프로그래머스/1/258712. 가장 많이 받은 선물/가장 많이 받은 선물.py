def solution(friends, gifts):
    # 이번달 까지 두 사람 사이에 더 많은 선물을 준 사람이 다음달에 선물을 하나 받음
    # gifts = [A B, ... B C] : A 선물을 준 사람, B 받은 사람
    # 선물을 주고 받은 횟수 카운트
    # 선물을 주고 받은 횟수를 2차원의 배열로
    N = len(friends)
    cnt = [[0]*N for _ in range(N)]
    for i in range(len(gifts)):
        A, B = gifts[i].split()
        r, c = friends.index(A), friends.index(B)
        
        cnt[r][c] += 1
        cnt[c][r] -= 1
    
    result = [0]*N
    for i in range(N):
        for j in range(N):
            if i == j: continue
            
            if cnt[i][j] > 0: result[i] += 1
            elif not cnt[i][j] and sum(cnt[i]) > sum(cnt[j]): result[i] += 1
    
    # 선물을 가장 많이 받을 친구가 받을 선물의 수
    answer = max(result)
    return answer