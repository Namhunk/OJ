def solution(coin, cards):
    n = len(cards) # 카드 개수
    target = n + 1 # 목표 숫자

    hand = cards[:n // 3] # 라운드 시작전 숫자
    pending = [] # 라운드 시작 이후 숫자
    idx = n // 3 # 시작 위치
    answer = 1 # 첫 라운드는 무조건 시작

    def use_pair(a, b): # 배열에 숫자가 있는지 검사
        for x in a[:]:
            y = target - x
            if y in b:
                a.remove(x)
                b.remove(y)
                return True
        return False

    while idx < n:
        pending.append(cards[idx])
        pending.append(cards[idx + 1])
        idx += 2

        if use_pair(hand, hand):
            answer += 1
        elif coin >= 1 and use_pair(hand, pending):
            coin -= 1
            answer += 1
        elif coin >= 2 and use_pair(pending, pending):
            coin -= 2
            answer += 1
        else:
            break

    return answer