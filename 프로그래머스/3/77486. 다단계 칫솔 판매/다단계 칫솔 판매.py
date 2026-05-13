# 1 <= len(enroll) <= 10,000
# len(referral) == len(enroll)

# 1 <= len(seller) < =100,00
# len(amount) == len(seller)

from collections import deque
from math import ceil, floor
def solution(enroll, referral, seller, amount):
    n = len(enroll)
    name2idx = {name: i for i, name in enumerate(enroll)}
    parent = [-1] * n
    for i, r in enumerate(referral):
        parent[i] = name2idx[r] if r != '-' else -1

    ans = [0] * n

    for s, a in zip(seller, amount):
        cur = name2idx[s]
        money = a * 100
        while cur != -1 and money > 0:
            give_up = money // 10
            keep = money - give_up
            ans[cur] += keep
            money = give_up
            cur = parent[cur]

    return ans

"""
enroll = 민호를 제외한 나머지 구성원 이름
referral[i] = i 위치의 부모 이름
seller[i] = i번째 개수를 누가 판매한건지
amount[i] = 판매량, amount[i] x 100

"""