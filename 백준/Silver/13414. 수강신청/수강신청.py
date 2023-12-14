import sys
from collections import defaultdict

k, l = map(int, sys.stdin.readline().strip().split())
student = defaultdict(int)
sequence = []

for _ in range(l):
    num = sys.stdin.readline().strip()
    sequence.append(num)
    student[num] += 1

cnt = k
for i in sequence:
    if not cnt: break
    student[i] -= 1
    if not student[i]: print(i); cnt -= 1
