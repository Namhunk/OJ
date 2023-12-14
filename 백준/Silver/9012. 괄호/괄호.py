import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    string = sys.stdin.readline().strip()
    stack = []
    for i in string:
        if i == "(": stack.append(i)
        elif i == ")":
            if len(stack) != 0: stack.pop()
            else: stack.append(i); break

    if len(stack) == 0: print("YES")
    else: print("NO")