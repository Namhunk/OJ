import sys

stack = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    command = sys.stdin.readline().strip()
    if "push" in command:
        k, v = command.split()
        stack.append(int(v))
    elif "pop" in command:
        if len(stack) != 0: print(stack.pop())
        else: print(-1)
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        if len(stack) == 0: print(1)
        else: print(0)
    elif "top" in command:
        if len(stack) == 0: print(-1)
        else: print(stack[-1])