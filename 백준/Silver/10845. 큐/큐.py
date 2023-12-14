import sys

que = []

N = int(sys.stdin.readline().strip())
for _ in range(N):
    command = sys.stdin.readline().strip()

    if "push" in command:
        c, i = command.split()
        que.append(i)
    elif "pop" in command:
        if len(que) != 0: print(que.pop(0))
        else: print(-1)
    elif "size" in command:
        print(len(que))
    elif "empty" in command:
        if len(que) == 0: print(1)
        else: print(0)
    elif "front" in command:
        if len(que) != 0: print(que[0])
        else: print(-1)
    elif "back" in command:
        if len(que) != 0: print(que[-1])
        else: print(-1)