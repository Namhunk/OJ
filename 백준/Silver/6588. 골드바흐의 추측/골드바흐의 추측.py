import sys, math

num = [False, False] + [True] * 1000000
s = [0] * 1000001
for i in range(2, int(len(num) ** 0.5)+1):
    if num[i]:
        for j in range(2 * i, len(num), i):
            num[j] = False

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0: break
    if n < 5 or n % 2 == 1: print("Goldbach's conjecture is wrong.")
    else:
        for i in range(n-1, n//2-1, -1):
            if s[n] != 0: print(f'{n} = {s[n][0]} + {s[n][1]}'); break
            elif num[i] and num[n-i]:
                s[n] = (n-i, i)
                print(f'{n} = {n-i} + {i}')
                break