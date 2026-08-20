from itertools import combinations
from bisect import bisect_left
from collections import defaultdict

def solution(info, query):
    answer = []
    score_map = defaultdict(list)

    for line in info:
        *conditions, score = line.split()
        score = int(score)

        for i in range(1 << 4):
            key = []
            for j in range(4):
                if i & (1 << j):
                    key.append('-')
                else:
                    key.append(conditions[j])
            score_map[' '.join(key)].append(score)

    for key in score_map:
        score_map[key].sort()

    for q in query:
        q = q.replace(' and ', ' ')
        *conditions, x = q.split()
        x = int(x)
        key = ' '.join(conditions)

        scores = score_map[key]
        idx = bisect_left(scores, x)
        answer.append(len(scores) - idx)

    return answer

"""
- 가 나오는 경우를 포함해서 

4 x 3 x 3 x 3 = 108개의 key값이 만들어짐
각 key마다 배열을 만든 뒤 해당 key에 속하는 info 값들의 점수를 추가
정렬 후 이분탐색으로 조건을 만족하는 길이를 찾음

"""