import sys

def hanoi(n, A, B, C):
    if n == 1: print(f'{A} {C}')
    else:
        hanoi(n-1, A, C, B)
        print(f'{A} {C}')
        hanoi(n-1, B, A, C)



n = int(sys.stdin.readline().strip())
print(2**n - 1)
hanoi(n, '1', '2', '3')
