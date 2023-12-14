x, y, w, h = map(int, input().split())

num = [x, y, w - x, h - y]
min = num[0]
for i in num:
    if i < min:
        min = i

print(min)