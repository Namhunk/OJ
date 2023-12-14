import sys

def H(n):
    k = list(map(int, " ".join(str(n)).split()))
    d = 0
    if len(k) > 1: d = k[1] - k[0]
    for i in range(len(k)):
        if k[i] != k[0] + (i * d): return False
    return True


N = int(sys.stdin.readline().strip())
count = 0
for i in range(1, N+1):
    if H(i): count += 1

print(count)