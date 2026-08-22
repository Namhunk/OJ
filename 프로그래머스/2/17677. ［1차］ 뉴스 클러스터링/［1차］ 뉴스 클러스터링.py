# 2 <= len(str) <= 1,000
# 글자 쌍을 만들때 알파벳으로 구성된 것만 사용 가능

from collections import defaultdict
def solution(str1, str2):
    answer = 0
    
    # 두 문자열을 모두 대문자로
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 집합 A 생성
    A = defaultdict(int)
    for i in range(1, len(str1)):
        key = str1[i-1]+str1[i]
        if key.isalpha():
            A[key] += 1
    
    # 집합 B 생성
    B = defaultdict(int)
    for i in range(1, len(str2)):
        val = str2[i-1]+str2[i]
        if val.isalpha():
            B[val] += 1
    
    M = 65536

    answer = int(J(A, B) * M)
    return answer

def J(A, B): # 다중 집합에 대한 원소 계산
    A_set = set(A.keys())
    B_set = set(B.keys())
    
    # AnB는 겹치는 key값을 추출해 둘 중 최소 계산
    AnB = 0
    AnB_keys = A_set & B_set
    for k in AnB_keys:
        AnB += min(A[k], B[k])
    
    # AuB는 모든 key값
    AuB = 0
    AuB_keys = A_set | B_set
    for k in AuB_keys:
        AuB += max(A[k], B[k])
    
    # 이떄 AnB, AuB 가 0인 경우 1로
    if AuB == 0:
        return 1
    
    return AnB / AuB
'''
자카드 유사도: 집합 A, B 사이의 유사도 = A n B / A u B


'''