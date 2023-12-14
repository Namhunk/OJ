import sys
N = int(sys.stdin.readline().strip())
num = []
x = 0
while True:
    if 5 * x > N: break
    a = N - (5 * x)
    if a % 3 == 0 and 5 * x <= N:
        y = (a//3)
        num.append(x+y)

    x += 1
print(min(num) if len(num) != 0 else -1)