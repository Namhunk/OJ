import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().strip().split())
alpha = list(sys.stdin.readline().strip().split())
alpha.sort()

alpha1 = []
alpha2 = []

for i in alpha:
    if i in 'aeiou': alpha1.append(i)
    else: alpha2.append(i)

k = []
for i in range(1, len(alpha1)+1 if l-len(alpha1)> 1 else l-1):
    for j in combinations(alpha1, i):
        for z in combinations(alpha2, l-i):
            k.append(sorted(list(j)+list(z)))

k.sort()
for i in k:
    print("".join(i))