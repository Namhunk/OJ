import sys

N = int(sys.stdin.readline().strip())

print(int("".join(sorted(list(" ".join(str(N)).split()), reverse=True))))