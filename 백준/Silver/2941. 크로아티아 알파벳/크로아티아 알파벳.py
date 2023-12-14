import sys

Alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = sys.stdin.readline().strip()
count = 0
stack = []
for i in word:
    stack += i
    count += 1
    for j in Alpha:
        if j in "".join(stack): count -= (len(j) - 1); stack.clear()

print(count)