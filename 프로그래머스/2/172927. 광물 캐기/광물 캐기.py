def solution(picks, minerals):
    answer = 0
    n = len(minerals)

    S2N = {"diamond": 100, "iron": 10, "stone": 1}  # 단어를 숫자로 변경(각 자릿수가 해당 광물 개수)
    arr = []
    curr = 0
    for i in range(n):
        name = minerals[i]
        curr += S2N[name]

        if (i + 1) % 5 == 0:  # 5개씩 묶음
            arr.append(curr)
            curr = 0

    if curr:  # n이 5로 나누어 떨어지지 않는 경우
        arr.append(curr)

    m = min(len(arr), sum(picks))  # 실제로 캘 수 있는 그룹 개수
    arr = arr[:m]                   # 원래 순서 기준으로 앞에서 m개만 남김

    arr = sorted(arr, reverse=True)  # 그 다음에야 피로도가 높은 순서로 정렬

    t = 0  # 곡괭이 idx (0=다이아, 1=철, 2=돌)
    f = 0  # arr idx
    while t < 3 and f < len(arr):  # 곡괭이가 남아있고, 광물이 남아있는 경우만
        if picks[t] <= 0:  # 현재 곡괭이를 다 쓴 경우
            t += 1
        else:  # 현재 곡괭이가 남은 경우
            picks[t] -= 1  # 1개 사용

            for i in range(2, -1, -1):  # 2 -> 0 (다이아 -> 철 -> 돌 자릿수)
                p = (10 ** i)
                c = arr[f] // p
                rp = (2 - i)
                m2 = max(1, 5 ** (t - rp))
                answer += c * m2
                arr[f] -= c * p

            f += 1

    return answer
'''
마인이 작업을 끝내기까지 필요한 최소한의 피로도

곡괭이의 개수 picks 0 = ida, 1 = iron, 2 = stone
광물들의 순서 minerals

피로도 표 (1, 1) 부터 다이아, 철, 돌 순서
1  1  1
5  1  1
25 5  1

각 곡괭이는 광물 5개를 캔 뒤 사라짐
----------------------------------------------------
각 광물을 길이 5씩 나눔

'''