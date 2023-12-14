import sys

n = int(sys.stdin.readline().strip())
ci = []
for _ in range(n):
    ci.append(int(sys.stdin.readline().strip()))

ci.sort(reverse= True)

for i in range(1, n+1):
    if i % 3 == 0: ci[i-1] = 0

print(sum(ci))