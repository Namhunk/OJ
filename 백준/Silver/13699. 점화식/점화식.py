import sys

t = [1] + [0] * 36
n = int(sys.stdin.readline().strip())

for i in range(1, len(t)):
    for j in range(i):
        t[i] += t[j] * t[i-j-1]

print(t[n])