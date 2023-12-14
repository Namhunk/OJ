import sys

w = ['CY', 'SK']
n = int(sys.stdin.readline().strip())
print(w[(n // 3 + n % 3) % 2])