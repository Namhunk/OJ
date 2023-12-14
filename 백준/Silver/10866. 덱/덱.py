import sys

deque = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    command = sys.stdin.readline().strip()

    if "push_front" in command:
        c, i = command.split()
        deque.insert(0, i)
    elif "push_back" in command:
        c, i = command.split()
        deque.append(i)
    elif "pop_front" in command:
        if len(deque) != 0: print(deque.pop(0))
        else: print(-1)
    elif "pop_back" in command:
        if len(deque) != 0: print(deque.pop())
        else: print(-1)
    elif "size" in command:
        print(len(deque))
    elif "empty" in command:
        if len(deque) != 0: print(0)
        else: print(1)
    elif "front" in command:
        if len(deque) != 0: print(deque[0])
        else: print(-1)
    elif "back" in command:
        if len(deque) != 0: print(deque[-1])
        else: print(-1)