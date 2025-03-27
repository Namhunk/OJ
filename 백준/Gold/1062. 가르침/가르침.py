import sys
input = sys.stdin.readline

# 단어의 개수 N, 글자의 수 K
N, K = map(int, input().strip().split())
words = [] # 각 단어에 포함된 글자를 저장
all_char = set() # 모든 단어의 글자
curr_char = set('acnit') # a c n i t 는 반드시 포함되어야 함

for _ in range(N):
    word = set(input().strip())
    words.append(word)
    all_char |= word

other = all_char - curr_char # 모든 단어의 글자들 중 a c n i t 가 아닌 글자들

from itertools import combinations
if K < 5: print(0) # a n c i t 를 포함할 수 없는 경우
elif len(other) <= K-5: print(N) # a c n i t를 제외한 구해야 하는 글자의 수가 K-5 보다 적은 경우
else:
    arr = combinations(other, len(other)-(K-5)) # 기본 글자를 제외한 집합에서 나머지를 뽑음
    ans = 0 # 결과값

    for x in arr:
        cnt = 0
        tmp = all_char - set(x) # 전체 글자에서 현재 글자들을 제외했을때 K개가 남음
        for y in words:
            if y <= tmp:
                cnt += 1

        ans = max(ans, cnt)

    print(ans)