A, B = map(int, input().split())
C = int(input())

h = (B + C) // 60
m = (B + C) % 60
if A + h >= 24:
    print((A + h) - 24, m)
else:
    print(A + h, m)