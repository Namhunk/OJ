import sys

l = []
for i in range(16):
    l.append("{" + ",".join(l[:i]) + "}")

for i in range(int(sys.stdin.readline().strip())):
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    print(l[l.index(a) + l.index(b)])