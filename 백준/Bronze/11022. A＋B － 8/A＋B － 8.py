dict = {}
for i in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    dict[i] = f'{a} + {b} = {a + b}'

for i in dict:
    print(f'Case #{i}: {dict[i]}')