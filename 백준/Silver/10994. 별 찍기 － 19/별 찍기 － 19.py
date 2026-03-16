import sys
input = sys.stdin.readline

def solve():
    # N(1 <= N <= 100)
    N = int(input().strip())

    arr = Star(N)
    for i in arr:
        print(i)

def Star(n):
    if n == 1: return ['*']
    else:
        before = Star(n-1)
        ret = []
        W = len(before)+4
        
        sub = ['*'*W, '*'+' '*(W-2)+'*']

        for i in sub:
            ret.append(i)
        
        for i in before:
            ret.append('* ' + i + ' *')
        
        for i in sub[::-1]:
            ret.append(i)
        
        return ret

   
if __name__ == '__main__':
    solve()

"""
4(n-1)

N=1
W=1, H=1

N=2
W=5, H=9

N=3
W=9, H=17

N=4
W=13, H=25

"""