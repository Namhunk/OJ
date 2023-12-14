import sys

n = int(sys.stdin.readline().strip())
book = list(int(sys.stdin.readline().strip()) for _ in range(n))
r = 0
fix = [book.index(n)]

for i in range(n-1, -1, -1):
    if i < fix[-1] and book[i] + 1 == book[fix[-1]]:
        fix.append(i)

print(n - len(fix))
