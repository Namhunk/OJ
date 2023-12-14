import sys

def is_prime(k):
    if k <= 1: return False

    for i in range(2, int(k ** 0.5) + 1):
        if not k % i: return False
    
    return True

def check(k):
    if len(str(k)) == n: print(k)

    else:
        for i in range(1, 10, 2):
            ans = k * 10 + i
            if is_prime(ans):
                check(ans)

n = int(sys.stdin.readline().strip())
for i in [2, 3, 5, 7]:
    check(i)