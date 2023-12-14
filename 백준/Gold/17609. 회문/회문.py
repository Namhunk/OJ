import sys

def check_pseudo_palindrome(arr, left, right):
    while left <= right:
        if arr[left] != arr[right]: return 2
        left += 1; right -= 1

    return 1


def check_palindrome(arr):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        if arr[left] != arr[right]:
            return min(check_pseudo_palindrome(arr, left + 1, right),\
                       check_pseudo_palindrome(arr, left, right - 1) )
        left += 1; right -= 1
        
    return 0

t = int(sys.stdin.readline().strip())
for _ in range(t):
    String = list(sys.stdin.readline().strip())
    print(check_palindrome(String))