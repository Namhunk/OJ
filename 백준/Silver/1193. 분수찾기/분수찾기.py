import sys

X = int(sys.stdin.readline().strip())
x = X
for i in range(1, x+1):
    if x > i:
        x -= i
    else:
        if i % 2 == 0: print(f'{x}/{(i+1) - x}'); break
        else: print(f'{(i+1)-x}/{x}'); break