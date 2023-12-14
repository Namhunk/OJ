import sys

def solve():
    m = int(sys.stdin.readline().strip())
    arr = []
    for _ in range(int(m//10)+1 if m % 10 else int(m//10)):
        arr.extend(list(map(int, sys.stdin.readline().strip().split())))
    
    s = set()
    num = 0
    for i in range(m):
        num += arr[i]
        s.add(num)

    
    for i in range(m, 0, -1):
        if num % i: continue
        plus = num // i
        temp, flag = 0, 1
        for j in range(i):
            temp += plus
            if temp not in s: flag ^= 1; break
        
        if flag: return plus

t = int(sys.stdin.readline().strip())
for _ in range(t):
    print(solve())