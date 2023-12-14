import sys, queue
que = queue.Queue(maxsize= 100)
for _ in range(int(sys.stdin.readline().strip())):
    num = 0
    N, M = map(int, sys.stdin.readline().strip().split())
    document = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(N):
        que.put((i, document[i]))
    while not que.empty():
        x, y = que.queue[0]
        if y < max(que.queue, key=lambda x: x[1])[1]: que.put(que.get())
        else:
            que.get()
            num += 1
            if x == M:print(num)
