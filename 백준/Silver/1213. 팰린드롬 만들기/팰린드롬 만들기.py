import sys

name = [i for i in sys.stdin.readline().strip()]
name.sort()

a = []
b = []
for i in range(len(name)):
    if i % 2 == 0: a.append(name[i])
    else: b.append(name[i])

k = ""
for i in range(len(b)):
    if a[i] != b[i]: k = a[i]; del a[i]; break

r = "".join(a) + k + "".join(b[::-1])
print(r if r == r[::-1] else "I'm Sorry Hansoo")