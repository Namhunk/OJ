import sys, math
s = ["***", "* *", "***"]

def print_stars(s):
    l = len(s)
    for i in range(l):
        s.append(s[i] + " " * l + s[i])
    for i in range(l):
        s.append(s[i]*3)
    for i in range(l):
        s[i] *= 3
    

N = int(sys.stdin.readline().strip())
for i in range(1, int(math.ceil(math.log(N, 3)))):
    if N > 3 and N % 3 == 0:
        print_stars(s)

for i in s:
    print(i)