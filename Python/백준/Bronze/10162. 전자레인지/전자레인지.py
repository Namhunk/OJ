import sys

ti = [10, 60, 300]
t = int(sys.stdin.readline().strip())
a=b=c=0
if t%ti[0] != 0: print(-1)
else:
    if t >= ti[2]: a+=(t//ti[2]); t%=ti[2]
    if t >= ti[1]: b+=(t//ti[1]); t%=ti[1]
    if t >= ti[0]: c+=(t//ti[0]); t%=ti[0]
    print(a,b,c)