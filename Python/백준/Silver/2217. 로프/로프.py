import sys

n = int(sys.stdin.readline().strip())
rope = list(int(sys.stdin.readline().strip()) for _ in range(n))
rope.sort()

max_w = []
for i in range(n):
    max_w.append(rope[i]*(n-i))

print(max(max_w))