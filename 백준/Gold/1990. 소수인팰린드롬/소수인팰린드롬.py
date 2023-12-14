import sys
input = sys.stdin.readline
#01
def sosu(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
a,b=map(int,input().split())
#02
if b>10000000:
    b=10000000
#03
arr=[n for n in range(a,b+1) if str(n)==str(n)[::-1]]
for n in arr:
    if sosu(n):
        print(n)
print(-1)
