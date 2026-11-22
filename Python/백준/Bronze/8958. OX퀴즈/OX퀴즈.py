N = int(input())
for i in range(N):
    S = input()
    num = 0
    p = 0
    for i in S:
        if i == "O":
            num += p + 1
            p += 1
        elif i == "X": p = 0
    print(num)