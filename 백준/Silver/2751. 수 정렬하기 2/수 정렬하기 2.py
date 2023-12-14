import sys
num = set()
for _ in range(int(sys.stdin.readline().strip())):
    a = int(sys.stdin.readline().strip())
    if abs(a) <= 1000000:
        num.add(a)

for i in sorted(list(num)):
    print(i)