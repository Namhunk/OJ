import sys

n = int(sys.stdin.readline().strip())

dance = set()
dance.add("ChongChong")
for _ in range(n):
    a, b = sys.stdin.readline().strip().split()

    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))