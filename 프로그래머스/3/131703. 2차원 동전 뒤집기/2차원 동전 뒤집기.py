INF = 10**9

def solution(beginning, target):
    R = len(beginning)
    C = len(beginning[0])

    ans = INF

    # 0 ~ (1<<R)-1: 뒤집을 행 집합을 비트마스크로 표현
    for mask in range(1 << R):
        row_flip_cnt = bin(mask).count("1")

        # 열 뒤집기 개수 세기
        col_flip_cnt = 0
        ok = True

        for c in range(C):
            # 해당 열의 (행 뒤집기까지 반영된) 현재 열과 타겟 열을 비교
            same = True
            opposite = True

            for r in range(R):
                # 행 r가 뒤집혔으면 1 - beginning[r][c], 아니면 그대로
                cur = beginning[r][c]
                if (mask >> r) & 1:
                    cur ^= 1

                if cur != target[r][c]:
                    same = False
                if (cur ^ 1) != target[r][c]:
                    opposite = False

                # 둘 다 이미 불가능이면 더 볼 필요 없음
                if not same and not opposite:
                    break

            if not same and not opposite:
                ok = False
                break
            elif opposite:
                # 완전히 반대라면, 이 열은 한 번 뒤집어야 함
                col_flip_cnt += 1
            # same인 경우는 열을 안 뒤집으면 됨

        if ok:
            ans = min(ans, row_flip_cnt + col_flip_cnt)

    return ans if ans != INF else -1