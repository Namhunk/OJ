import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().strip().split())

Dict = defaultdict(int)
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        Dict[word] += 1

ans = sorted(Dict.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))

for i in ans:
    print(i[0])