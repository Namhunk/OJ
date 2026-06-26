from collections import deque

def solution(rc, operations):
    R = len(rc)
    C = len(rc[0])

    # 왼쪽 / 가운데 / 오른쪽 분리
    left = deque()
    mid = deque()
    right = deque()

    for r in range(R):
        left.append(rc[r][0])
        mid.append(deque(rc[r][1:C-1]))
        right.append(rc[r][C-1])

    # 연산 수행
    for op in operations:
        if op == "ShiftRow":
            left.appendleft(left.pop())
            mid.appendleft(mid.pop())
            right.appendleft(right.pop())
        else:  # "Rotate"
            mid[0].appendleft(left.popleft())
            right.appendleft(mid[0].pop())
            mid[-1].append(right.pop())
            left.append(mid[-1].popleft())

    # 행렬로 복원
    answer = []
    for r in range(R):
        answer.append([left[r]] + list(mid[r]) + [right[r]])
    return answer

        
'''
shiftRow: 모든 행이 아래로 한 칸씩 밀려남

Rotate: 행렬의 바깥쪽에 있는 원소를 시계 방향으로 한 칸 회전

연산을 시행한 후 행렬상태를 return



'''