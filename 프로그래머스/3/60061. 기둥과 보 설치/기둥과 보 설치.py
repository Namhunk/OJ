# 5 <= n <= 100
# 1 <= len(build_frame) <= 1,000
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        
        if b == 1:  # 설치
            answer.append([x, y, a])
            if not is_valid(answer):  # 전체 검증
                answer.remove([x, y, a])
        else:  # 삭제
            answer.remove([x, y, a])
            if not is_valid(answer):  # 전체 검증
                answer.append([x, y, a])
    
    return sorted(answer)

def is_valid(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            # 바닥 or 기둥 위 or 보 위(왼쪽/오른쪽)
            if y == 0 or [x, y-1, 0] in answer or \
               [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        else:  # 보
            # 한쪽 끝이 기둥 위 or 양쪽 끝이 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or \
               ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


"""
기둥, 보 = 각 길이가 1인 선분
- 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 다른 기둥 위에 있어야 함
- 보는 한쪽 끝 부분이 기둥위에 있거나, 양쪽 끝 부분이 다른 보와 연결되어야 함
- 보는 바닥에 설치가 불가능

최종 구조물은
길이가 3인 2차원 배열 [x, y, a]
x, y 기둥, 보의 교차점 좌표

build_frame의 순서대로 구조물을 설치할 때 조건을 만족하는지 확인 후 추가

"""