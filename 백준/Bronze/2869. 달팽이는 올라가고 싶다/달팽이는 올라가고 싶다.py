import math
a,b,v = map(int, input().split())
x = (v - b) / (a - b)
print(math.ceil(x))