A, B = input().split()
print(max(int("".join(reversed(A))), int("".join(reversed(B)))))