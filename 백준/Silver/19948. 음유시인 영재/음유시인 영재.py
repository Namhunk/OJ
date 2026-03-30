import sys
input = sys.stdin.readline

from string import ascii_uppercase
def solve():
    # 시의 내용
    S = list(input().strip().split())

    # 스페이스 바의 남은 사용 가능 횟수
    SPACE = int(input().strip())

    # 26개의 알파벳에 대한 영자판의 남은 사용가능 횟수
    ALPHA_CNT = list(map(int, input().strip().split()))

    # 각 알파벳에 대한 IDX 매칭
    ALPHA_TO_IDX = {j: i for i, j in enumerate(ascii_uppercase)}

    # 공백의 개수에 대한 검사(단어의 개수 - 1 이 공백의 개수임)
    if len(S)-1 > SPACE: return -1

    ans = '' # 조건을 만족할시 출력할 정답
    # 제목에 대한 검사
    for word in S:
        # ans가 비어있는 경우 첫 단어 추가
        curr = word[0].upper()

        if not len(ans):
            ans += curr
            idx = ALPHA_TO_IDX[curr]
            ALPHA_CNT[idx] -= 1
            continue
        
        if ans[-1] != curr:
            idx = ALPHA_TO_IDX[curr]
            ALPHA_CNT[idx] -= 1

        ans += curr
    
    # 내용에 대한 검사
    for word in S:
        # 첫 단어에 대한 계산
        before = word[0]
        idx = ALPHA_TO_IDX[before.upper()]
        ALPHA_CNT[idx] -= 1

        for c in word[1:]:
            if before != c: # 두 문자가 다른 경우
                before = c
                idx = ALPHA_TO_IDX[before.upper()]
                ALPHA_CNT[idx] -= 1
    
    if min(ALPHA_CNT) < 0: # 최솟값이 0보다 작으면
        return -1
    else:
        return ans

if __name__ == '__main__':
    print(solve())

"""
시의 내용과 제목을 모두 기록할 수 있다면 시의 제목을 출력
기록을 못한다면 -1 출력

시에 나오는 단어들의 첫 글자는 대문자

1. 시의 내용을 공백을 기준으로 분리하여 개수가 SPACE의 값 이하인지 확인

2. 각 문자가 연속되는지 확인
    2-1. 제목에서 연속하는지
    2-2. 내용에서 연속하는지

"""