import sys, math

n = int(sys.stdin.readline().strip())
arr = [sys.stdin.readline().strip() for _ in range(n)]
T = ""

def check(left, right):
    while left <= right:
        if arr[left] < arr[right]: return True
        elif arr[left] > arr[right]: return False
        else:
            left += 1; right -= 1
    
    return True

left, right = 0, n-1
while left <= right:
    if arr[left] < arr[right]:
        T += arr[left]
        left += 1
    elif arr[left] > arr[right]:
        T += arr[right]
        right -= 1
    else:
        if check(left + 1, right - 1):
            T += arr[left]
            left += 1
        else:
            T += arr[right]
            right -= 1

for i in range(math.ceil(len(T)/80)):
    print(T[i*80: min((i+1)*80, len(T))])
