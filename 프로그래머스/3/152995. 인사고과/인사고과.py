def solution(scores):
    n = len(scores)
    a0, b0 = scores[0]

    # a 내림차순, 같으면 b 내림차순 정렬 (인덱스 포함)
    order = sorted(range(n), key=lambda i: (-scores[i][0], -scores[i][1]))

    use = [True] * n
    max_b = -1
    i = 0
    while i < n:
        j = i
        # 같은 a값인 그룹을 한 번에 처리
        while j < n and scores[order[j]][0] == scores[order[i]][0]:
            idx = order[j]
            if scores[idx][1] < max_b:
                use[idx] = False
            j += 1
        # 그룹 처리 끝난 뒤 max_b 갱신 (그룹 내부는 서로 영향 X)
        for k in range(i, j):
            max_b = max(max_b, scores[order[k]][1])
        i = j

    if not use[0]:
        return -1

    answer = 1
    curr = a0 + b0
    for i in range(1, n):
        if use[i] and curr < scores[i][0] + scores[i][1]:
            answer += 1

    return answer