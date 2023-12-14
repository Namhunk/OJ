import sys, heapq

T = int(sys.stdin.readline().strip())
for _ in range(T):
    k = int(sys.stdin.readline().strip())
    length = [0] * (int(1e6)+1)
    MIN_Q = []
    MAX_Q = []

    for i in range(k):
        cmd = list(sys.stdin.readline().strip().split())
        cmd[1] = int(cmd[1])

        if cmd[0] == 'I':
            heapq.heappush(MIN_Q, (cmd[1], i))
            heapq.heappush(MAX_Q, (-cmd[1], i))
            length[i] = 1
        
        elif cmd[1] == 1:
            while MAX_Q and not length[MAX_Q[0][1]]: heapq.heappop(MAX_Q)
            if MAX_Q:
                length[MAX_Q[0][1]] = 0
                heapq.heappop(MAX_Q)
        
        else:
            while MIN_Q and not length[MIN_Q[0][1]]: heapq.heappop(MIN_Q)
            if MIN_Q:
                length[MIN_Q[0][1]] = 0
                heapq.heappop(MIN_Q)
        while MIN_Q and not length[MIN_Q[0][1]]: heapq.heappop(MIN_Q)
        while MAX_Q and not length[MAX_Q[0][1]]: heapq.heappop(MAX_Q)
    
    if not MIN_Q: print("EMPTY")
    else: print(-MAX_Q[0][0], MIN_Q[0][0])