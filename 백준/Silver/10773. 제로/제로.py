import sys
K = int(sys.stdin.readline().strip())
stack = []
for _ in range(K):
    N = int(sys.stdin.readline().strip())
    if N == 0: stack.pop()
    else: stack.append(N)

print(sum(stack))