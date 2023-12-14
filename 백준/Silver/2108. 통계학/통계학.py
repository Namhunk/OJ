import sys
N = int(sys.stdin.readline().strip())
numbers = []
count = [0 for _ in range(-4000, 4001)]
sequence = []
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    count[4000 + num] += 1
big = max(count)
for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            numbers.append(i - 4000)
        if count[i] == big:
            sequence.append(i - 4000)


print(round(sum(numbers) / N))
print(numbers[N // 2])
print(sequence[0] if len(sequence) == 1 else sequence[1])
print(max(numbers) - min(numbers))