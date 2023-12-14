import sys

set_price = 0
b = d = 2000
for i in range(3):
    burger = int(sys.stdin.readline().strip())
    if burger < b: b = burger

set_price += b

for i in range(2):
    drink = int(sys.stdin.readline().strip())
    if drink < d: d = drink

set_price += d

print(set_price-50)