import sys

for _ in range(int(sys.stdin.readline().strip())):
    A, B = map(int, sys.stdin.readline().strip().split())
    a = A; b = B
    while a % b != 0 if a > b else b % a != 0:
        if a > b and a % b != 0:
            a %= b
        elif a < b and b % a != 0:
            b %= a

    print(int((A * B) / (a if a < b else b)))