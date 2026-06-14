# 1 <= A == B <= 100,000
# 1 <= A[i], B[i] <= 1,000,000,000
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    a, b = 0, 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1
        
    return answer

'''
결국 A가 어떤 순서로 팀원을 배치해도
B는 A의 순서에 맞춰서 팀원을 배치함

A, B 정렬
순서대로 점수 확인


'''