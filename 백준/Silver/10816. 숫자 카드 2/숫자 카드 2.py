import sys
card = [0 for _ in range(-10000000, 10000001)]
N = int(sys.stdin.readline().strip())
Num = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
Mum = list(map(int, sys.stdin.readline().strip().split()))

for i in Num:
    card[i] += 1

for i in Mum:
    print(card[i], end =' ')