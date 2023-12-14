import sys

s = int(sys.stdin.readline().strip())
i = 1
while True:
    if i == int((s*2-i)**0.5):
        break
    i+=1
print(i)