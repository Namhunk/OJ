import sys

c = [0, 1, 2, 4]
for i in range(4, 12):
    c.append(c[i-1] + c[i-2] + c[i-3])

for i in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())

    print(c[n])