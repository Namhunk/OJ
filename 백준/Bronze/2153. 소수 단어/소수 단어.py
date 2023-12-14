import sys
INF = sys.maxsize
word = sys.stdin.readline().strip()
n = 0
for i in word:
    if ord(i) // 96 > 0:
        n += (ord(i) % 97 + 1)
    else:
        n += (ord(i) % 65 + 27)
k = 0
for i in range(2, n):
    if n % i == 0: k = 1; break

print('It is a prime word.' if k == 0 else 'It is not a prime word.')