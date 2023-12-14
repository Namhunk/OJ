import sys

n = int(sys.stdin.readline().strip())
file = {}

for _ in range(n):
    a, b = sys.stdin.readline().strip().split(".")

    if b not in file: file[b] = list(); file[b].append(a)
    else: file[b].append(a)

for i in sorted(file.keys()):
    print(i, len(file[i]))