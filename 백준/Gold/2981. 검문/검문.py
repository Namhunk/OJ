import sys, math
nums = sorted((int(sys.stdin.readline().strip()) for _ in range(int(sys.stdin.readline().strip()))))
A = []
for i in range(len(nums)-1):
    A.append(nums[i+1]-nums[i])

p = [math.gcd(*A)]
for i in range(2, int(math.sqrt(p[0]))+1):
    if math.gcd(*A)%i == 0:
        p.append(i)
        p.append(math.gcd(*A)//i)

print(*sorted(set(p)))