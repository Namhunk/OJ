import sys

s = sys.stdin.readline().strip()
rs = 1
for i in range(1, len(s)):
    if s[i-1] != s[i]: rs += 1

print(rs//2)