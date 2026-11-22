import sys

v = [0,0]

for _ in range(int(sys.stdin.readline().strip())):
    s = int(sys.stdin.readline().strip())
    v[s]+=1

print("Junhee is not cute!" if v[0] > v[1] else "Junhee is cute!")
