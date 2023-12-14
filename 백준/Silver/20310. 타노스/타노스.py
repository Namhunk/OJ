import sys

s = sys.stdin.readline().strip()

c0 = s.count("0")//2
c1 = s.count("1")//2

dix = []

for i in range(len(s)):
    if c1 == 0:
        break

    if s[i] == "1":
        dix.append(i)
        c1 -= 1

for i in range(len(s)-1, -1, -1):
    if c0 == 0:
        break

    if s[i] == "0":
        dix.append(i)
        c0 -= 1
dix.sort()
ci = 0
ns = ""
for i in dix:
    ns += ''.join(s[ci:i])
    ci = i+1

ns += ''.join(s[ci:])
print(ns)