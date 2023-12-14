S = input()
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in S: print(S.index(i), end=" ")
    else: print(-1, end=" ")