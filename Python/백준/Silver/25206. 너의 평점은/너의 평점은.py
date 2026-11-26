import sys
import random, math
input = sys.stdin.readline

    
def solve():
    pass

def main():
    cnt = 0
    tot = 0
    grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

    tot = 0
    ans = 0
    for _ in range(20):
        _, a, b = input().strip().split()

        if b == 'P': continue
        a = float(a)
        tot += a
        ans += (a * grade[b])


    print(f'{round(ans / tot, 6):.6f}')
        


if __name__ == '__main__':
    main()  

"""


"""