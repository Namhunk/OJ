# 1 <= n <= 200
# 1 <= weak[i] <= 15
# 1 <= dist[i] <= 8

from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 1. 원형을 직선으로 펴기
    extended = weak + [w + n for w in weak]

    answer = len(dist) + 1  # 최대로 필요한 친구 수보다 큰 값으로 초기화

    # 2. 시작 약점 인덱스를 하나씩 잡기
    for start in range(length):
        # 3. 친구 순서를 모든 permutation으로 탐색
        for friends in permutations(dist, len(dist)):
            count = 1  # 투입한 친구 수
            # 첫 번째 친구가 커버할 수 있는 최대 위치
            pos = extended[start] + friends[count - 1]

            # 4. 현재 친구로 최대한 많이 커버
            for idx in range(start, start + length):
                # 이 약점이 현재 친구 범위 밖이면, 다음 친구 투입
                if extended[idx] > pos:
                    count += 1
                    # 더 이상 친구가 없으면 실패
                    if count > len(dist):
                        break
                    # 새 친구가 커버할 수 있는 최대 위치 갱신
                    pos = extended[idx] + friends[count - 1]

            # 모든 약점을 커버했다면, 최소 친구 수 갱신
            if count <= len(dist):
                answer = min(answer, count)

    # 5. 어떤 경우도 성공 못하면 -1
    if answer == len(dist) + 1:
        return -1
    return answer

'''
1시간 동안 취약 지점을 점검하기 위해 보내야 할 사람 수의 최솟값
n: 외벽 둘레
weak: 방문해야 하는 지점의 idx
dist: 1시간 동안 각 사람이 움직일 수 있는 거리

취약 지점은 최대 15개
사람은 최대 8명
이동 거리는 최대 100
--------------------------------------------------------

'''