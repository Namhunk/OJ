# 1 <= numbers <= 10,000
# 1 <= numbers[i] <= 10^15
def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(check(num))
    return answer

def check(x):
    cnt = len(bin(x)[2:])
    tot = 0
    while tot < cnt:
        tot = tot*2 + 1

    S = '0'*(tot-cnt) + bin(x)[2:]
    
    return 1 if tree(0, len(S)-1, S) else 0

def tree(l, r, S):
    if l == r:
        return True
    
    m = (l + r) // 2
    
    left_m = (l + m - 1) // 2
    right_m = (m + 1 + r) // 2
    
    if S[m] == '0' and (S[left_m] == '1' or S[right_m] == '1'):
        return False

    left = tree(l, m - 1, S)
    right = tree(m + 1, r, S)
    
    return left and right
    
"""
1. 이진수를 저장할 빈 문자열 생성
2. 주어진 이진트리에 더미 노드 추가
3. 포화 이진트리의 노드들을 가장 왼쪽부터 오른쪽 까지
    순서대로 살펴봄 높이는 영향 x
4. 살펴본 노드가 더미 노드라면 문자열 뒤에 0을 추가
    더미가 아니라면 1을 추가
5. 문자열에 저장된 이진수를 십진수로 변환
----------------------------------------
각 numbers[i]가 주어졌을 때
포화 이진 트리로 표현할 수 있는지 확인

1. 주어진 numbers[i]를 이진수로 변환
2. 더미노드를 포함한 총 노드의 개수는 2^n - 1 개
3. 이때 리프 노드를 제외하고 부모 노드에 더미노드가 있으면 안됨


"""