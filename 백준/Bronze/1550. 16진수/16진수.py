import sys
n = sys.stdin.readline().strip()
d = ['0', '1', '2', '3', '4', '5','6','7','8','9','A','B', 'C'
     ,'D', 'E','F']
s = 0
for i in range(len(n)):
    s += d.index(n[i]) * (16**(len(n)- 1 - i))
print(s)
