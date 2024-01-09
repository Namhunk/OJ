import sys

def print_seq(seq, x, cnt):
    if cnt == M: print(*seq)
    else:
        for i in range(x, len(arr)):
            print_seq([*seq, arr[i]], i, cnt+1)

# N, M 입력
N, M = map(int, sys.stdin.readline().strip().split())
arr = sorted(list(set(map(int, sys.stdin.readline().strip().split()))))

for i in range(len(arr)):
    print_seq([arr[i]], i, 1)