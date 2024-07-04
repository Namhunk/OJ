def solution(bandage, health, attacks):
    answer = 0
    hp = health
    heal = 0
    time = 0
    before = 0
    for t, at in attacks:
        if hp < health:
            time = t-before-1
            heal = time*bandage[1] + (time//bandage[0]*bandage[2])
            hp = min(hp+heal, health)
        
        hp -= at
        if hp <= 0: break
        before = t
        
    answer = (-1 if hp <= 0 else hp)
    return answer