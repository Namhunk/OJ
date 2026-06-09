def solution(n, k, cmd):
    cur = k                          # 현재 커서 위치
    table = {i: [i - 1, i + 1] for i in range(n)}  # 각 행의 [prev, next]
    table[0][0] = None               # 첫 행의 prev는 없음
    table[n - 1][1] = None           # 마지막 행의 next는 없음

    answer = ['O'] * n               # 삭제 여부 표시
    stack = []                       # 삭제된 행 정보 스택

    for c in cmd:
        # 삭제
        if c == "C":
            answer[cur] = 'X'
            prev, nxt = table[cur]
            stack.append((prev, cur, nxt))

            # 링크 끊기
            if prev is not None:
                table[prev][1] = nxt
            if nxt is not None:
                table[nxt][0] = prev

            # 커서 이동: 아래가 있으면 아래로, 아니면 위로
            if nxt is not None:
                cur = nxt
            else:
                cur = prev

        # 복구
        elif c == "Z":
            prev, now, nxt = stack.pop()
            answer[now] = 'O'

            # 양쪽 노드와 다시 연결
            if prev is not None:
                table[prev][1] = now
            if nxt is not None:
                table[nxt][0] = now
            table[now] = [prev, nxt]

        # 위/아래 이동
        else:
            op, x = c.split()
            x = int(x)
            if op == 'U':
                for _ in range(x):
                    cur = table[cur][0]
            else:  # 'D'
                for _ in range(x):
                    cur = table[cur][1]

    return ''.join(answer)