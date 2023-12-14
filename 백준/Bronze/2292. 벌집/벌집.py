n = int(input())
r = 1
while n != 1:
    if n >= (3 * (r - 1)) * r + 2 and n <= (3 * r) * (r + 1) + 1:
        break
    r += 1

print(r +1 if n != 1 else 1)
