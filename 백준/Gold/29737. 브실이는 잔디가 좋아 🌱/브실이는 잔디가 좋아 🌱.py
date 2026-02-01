import sys
input = sys.stdin.readline

def user_streak(arr, W, name):
    # (7, W) -> (, 7*W) 변경
    logs = []
    for w in range(W):
        for d in range(7):
            logs.append(arr[d][w])
    
    MSL = 0 # streak 최대 길이
    F  = 0 # freeze 최소 사용
    S   = float('inf') # 스트릭 시작일
    X   = 0 # X 개수

    # 임시로 저장할 변수
    TMSL = 0
    TF   = 0
    TS   = float('inf')
    PF   = 0 # 다음 문자가 O or X 둘 중 어떤것이냐에 따라 추가할지 말지 결정

    for i, status in enumerate(logs, start=1):
        if status == 'O':
            if TMSL == 0: # 현재 스트릭 길이가 0인 경우
                TS = i # 시작 위치 i

            TMSL += 1 # 스트릭 길이 + 1
            TF += PF
            PF = 0

        elif status == 'F':
            if TMSL > 0: # 길이가 1 이상인 경우만
                PF += 1
            
        else: # status == 'X'
            if TMSL > MSL: # 전체 길이보다 긴 경우
                MSL = TMSL
                S = TS
                F = TF
            elif TMSL == MSL: # 길이는 같지만 F의 개수가 더 적은 경우
                if TF < F:
                    F = TF
                    S = TS
            
            TMSL = 0
            TF = 0
            PF = 0
            TS = float('inf')
            X += 1
    
    if TMSL > MSL:
        MSL = TMSL
        S = TS
        F = TF
    elif TMSL == MSL:
        if TF < F:
            F = TF
            S = TS
    
    return (-MSL, F, S, X, name)

N, W = map(int, input().strip().split())
rank = []

for _ in range(N):
    name = input().strip()
    arr = [list(input().strip()) for _ in range(7)]
    rank.append(user_streak(arr, W, name))

rank.sort()

if N > 0: # 위 순위 결정에도 순위가 같다면 순위는 같게 하고 닉네임의 사전 순으로 출력하며 그다음 순위는 이전 순위에 1을 더한 값으로 한다. 
    curr_rank = 1
    print(f'{curr_rank}. {rank[0][4]}')
    
    for i in range(1, N):
        if rank[i-1][:4] != rank[i][:4]:
            curr_rank += 1
        print(f'{curr_rank}. {rank[i][4]}')