# 1 <= len(user_id) <= 8
# 1 <= len(user_id[i]) <= 8

from itertools import combinations, permutations
def solution(user_id, banned_id):
    answer = 0
    S = set()
    
    for seq in permutations(user_id, len(banned_id)):
        flag = True
        for j, ID in enumerate(seq):
            if len(ID) != len(banned_id[j]):
                flag = False
                break
            
            for k in range(len(ID)):
                if banned_id[j][k] == '*': continue
                if ID[k] != banned_id[j][k]:
                    flag = False
                    break
            
            if not flag: break
        
        if flag:
            seq = sorted(seq)
            seq = tuple(seq)
            S.add(seq)
    
    # print(S)
    answer = len(S)
    return answer

"""
user_id에서 banned_id 를 보고

제외해야할 ID의 목록 개수를 반환

1. banned_id[i]의 길이와 같아야함
2. '*'을 제외한 위치에서 같아야 함
3. 이전에 포함된 ID는 제외

"""