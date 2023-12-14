import sys

l, r = map(int, sys.stdin.readline().strip().split())

cnt = 0
for i in range(len(str(l))):
    if str(l)[i] == str(r)[i]:
        if str(l)[i] == "8": cnt += 1
    else: break

print(cnt if len(str(l)) == len(str(r)) else 0)
