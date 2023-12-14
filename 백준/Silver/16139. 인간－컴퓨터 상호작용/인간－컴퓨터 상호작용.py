import sys

# len(알파벳) = 26
s = sys.stdin.readline().strip()
arr = [[0]*(len(s)+1) for _ in range(26)]

for i in range(len(s)):
    arr[ord(s[i])-97][i+1] += 1

for i in range(26):
    for j in range(1, len(s)+1):
        arr[i][j] += arr[i][j-1]

q = int(sys.stdin.readline().strip())
for _ in range(q):
    a, l, r = sys.stdin.readline().strip().split()

    print(arr[ord(a) - 97][int(r)+1] - arr[ord(a) - 97][int(l)])
