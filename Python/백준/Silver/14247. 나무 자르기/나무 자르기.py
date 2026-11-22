import sys
n = int(sys.stdin.readline().strip())
h = list(map(int, sys.stdin.readline().strip().split()))
a = list(map(int, sys.stdin.readline().strip().split()))

tree = [(a[i], h[i]) for i in range(n)]
tree.sort()

r = tree[0][1]
for i in range(1, n):
    r += tree[i][1] + tree[i][0] * i

print(r)
