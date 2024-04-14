import sys

def change(x, cnt):
    global ans
    if x > B: return
    if x == B: ans = min(ans, cnt)

    change(x*2, cnt+1)
    change(x*10 + 1, cnt+1)

A, B = map(int, sys.stdin.readline().strip().split())
ans = float('inf')

change(A, 0)
print(ans+1 if ans != float('inf') else -1)