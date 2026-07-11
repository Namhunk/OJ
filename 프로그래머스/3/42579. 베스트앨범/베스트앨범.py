from heapq import heappush, heappop
# 1. key값은 장르 이름, values는 리스트를 갖는 딕셔너리 생성
# 2. 주어진 배열의 값을 딕셔너리에 추가 하며 각 장르의 재생 횟수 합을 구함
# 3. 장르의 재생 횟수 합 값을 정렬(내림차순)
# 4. 정렬된 장르를 순서대로 돌며 각 장르의 값을 최소 1개 최대 2개를 가져옴
# 5. 정렬을 여러번 하는것보다 heap을 쓰는 방향으로
def solution(genres, plays):
    n = len(genres)
    names = {g: [] for g in set(genres)} # 장르 이름: 리스트
    totals = {g: 0 for g in set(genres)}
    for i in range(n):
        heappush(names[genres[i]], (-plays[i], i))
        totals[genres[i]] += plays[i]
    
    seq = sorted([(t, g) for g, t in totals.items()], reverse=True)
    answer = []
    for _, g in seq:
        for _ in range(min(2, len(names[g]))):
            _, idx = heappop(names[g])
            answer.append(idx)
    
    return answer

'''
노래 장르를 나타내는 문자열 배열과, 재생 횟수를 나타내는 배열이 주어질때
베스트 앨범에 들어갈 노래 번호를 return

1. 가장 많이 재생된 장르를 먼저 수록
2. 장르 내에서 많이 재생된 노래를 수록
3. 횟수가 같다면 고유번호가 작은 곡 수록

장르별로 2개씩 수록


'''