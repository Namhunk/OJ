import sys
counts = [0] * 10001
for _ in range(int(sys.stdin.readline().strip())):
    counts[int(sys.stdin.readline().strip())] += 1

for i in range(10001):
    for _ in range(counts[i]):
        print(i)