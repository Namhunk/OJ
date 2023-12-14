import sys

cal = []
nums = []

s = sys.stdin.readline().strip()
x = ""

for i in s:
    if i in '+-': cal.append(i); nums.append(int(x)); x = ""
    else: x += i
nums.append(int(x))

m = 0
for i in range(len(cal)):
    if cal[i] == '-': m += sum(nums[i+1:]); break

print(sum(nums)-(2*m))