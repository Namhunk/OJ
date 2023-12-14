H, M = map(int, input().split())
if M >= 45:
    print(H, M - 45)
elif M < 45:
    if H >= 1:
        print(H - 1, 60 + (M - 45))
    elif H < 1:
        print(24 + (H - 1), 60 + (M - 45))