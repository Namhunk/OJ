# 1 <= k <= 10^12 : 전체 방 개수
# 1 <= len(room_number) <= 200,000

def solution(k, room_number):
    connect = {}
    answer = []

    for num in room_number:
        path = []  # 거쳐간 방들 기록
        curr = num

        # 비어있는 방 찾기
        while curr in connect:
            path.append(curr)
            curr = connect[curr]

        # curr가 비어있는 방
        answer.append(curr)
        if curr < k:
            connect[curr] = curr + 1  # 이 방은 이제 꽉 찼으니, 다음 방을 가리키게

        # 경로 압축: 지나온 모든 방도 한 번에 curr+1을 가리키게
        nxt = curr + 1
        for p in path:
            connect[p] = nxt

    return answer

        
'''
각 고객에게 배정되는 방 번호를 순서대로 return

규칙
1. 한 번에 신청 순으로 방 배정
2. 고객은 원하는 방 번호 제출
3. 해당 방이 비어있다면 배정
4. 고객이 원하는 방이 있다면 크기가 크면서 비어있는 방 중 가장 작은 번호
--------------------------------------------------------------
예제를 기준으로
'''