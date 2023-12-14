import sys

n = int(sys.stdin.readline().strip())
card = list(map(int, sys.stdin.readline().strip().split()))

your_card = sum(card[1::2])

ans = sum(card[::2])
stack = 0
temp = 0

for i in range(n-1):
    if not i % 2:
        stack += card[i]
        ans = max(ans, stack - card[i] + your_card - temp)
    else:
        temp += card[i]
        ans = max(ans, stack + (your_card - temp + card[i] - card[n-1]))

print(ans)