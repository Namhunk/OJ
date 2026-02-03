import sys
input = sys.stdin.readline

"""
춘배가 가질 수 있는 최대 체력을 출력. 답이 0 이하일 경우 -1 출력

주어진 R[i]에서 춘배와 나비 사이의 거리를 뺀 값만큼 춘배의 체력이 깎인다.

1. 웅크리기: 나비의 공격데미지 절반 감소
2. 네발로 걷기: 나비와 거리가 멀어짐
3. 깜짝 놀라게 하기: i턴에 사용시 i+1턴의 나비의 행동 무시
"""

def skill_1(dist, surp, hp, K, R, i): # 웅크리기
    dmg = max(0, (R[i] - dist)//2)
    next_hp = hp - dmg

    return dist, surp, next_hp

def skill_2(dist, surp, hp, K, R, i): # 네발로 걷기
    next_dist = (dist + K)
    dmg = max(0, (R[i] - next_dist))
    next_hp = hp - dmg

    return next_dist, surp, next_hp

def skill_3(dist, surp, hp, K, R, i):
    dmg = max(0, (R[i] - dist))
    next_hp = hp - dmg

    surp = min(surp+1, 2)
    return dist, surp, next_hp

def check_key_hp(key, hp, states, i):
    if hp > 0:
        if key not in states[i] or states[i][key] < hp:
            return True
    
    return False

# 나비가 지칠 때까지의 냥냥펀치 수 (1 <= N <= 18)
N = int(input().strip())

# 춘배의 체력, 나비 사이의 거리, 네발로 걷기 시 이동하는 거리
# (1 <= H <= 1000, 1 <= D <= 10, 1 <= K <= 3)

H, D, K = map(int, input().strip().split())

# 데미지 R[i]
R = [0] + [int(input().strip()) for _ in range(N)]

states = [{} for _ in range(N+1)] # 모든 상태를 저장
states[0][(D, 0)] = H # (거리, 깜놀 사용 여부) # 깜놀: (0: 사용안함, 1: 다음 턴 무시 준비, 2: 무시 완료)

for i in range(1, N+1):
    for key, hp in states[i-1].items():
        dist, surp = key

        if surp == 1: # 이전턴에 깜놀 사용시 현재 나비의 공격 무시
            # 웅크리기
            key1 = (dist, surp+1)
            hp1 = hp
            if check_key_hp(key1, hp1, states, i):
                states[i][key1] = hp1
            
            # 네발로 걷기
            dist2, _, _ = skill_2(dist, surp, hp, K, R, i)
            key2 = (dist2, surp+1)
            hp2 = hp
            if check_key_hp(key2, hp2, states, i):
                states[i][key2] = hp2
        else:
            # 웅크리기
            dist1, surp1, hp1 = skill_1(dist, surp, hp, K, R, i)
            key1 = (dist1, surp1)
            if check_key_hp(key1, hp1, states, i):
                states[i][key1] = hp1
            
            # 네발로 걷기
            dist2, surp2, hp2 = skill_2(dist, surp, hp, K, R, i)
            key2 = (dist2, surp2)
            if check_key_hp(key2, hp2, states, i):
                states[i][key2] = hp2
            
            # 깜놀
            dist3, surp3, hp3 = skill_3(dist, surp, hp, K, R, i)
            key3 = (dist3, surp3)
            if check_key_hp(key3, hp3, states, i):
                states[i][key3] = hp3

if states[-1]:
    print(max(states[-1].values()))
else:
    print(-1)