import sys

S = sys.stdin.readline().strip()
l = set()
for i in range(len(S)+1):
    for j in range(i+1, len(S)+1):
        l.add(S[i:j])

print(len(l))