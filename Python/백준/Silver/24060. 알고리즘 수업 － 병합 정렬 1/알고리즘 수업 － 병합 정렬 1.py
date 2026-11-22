import sys

def merge_sort(A):
    if len(A) < 2: return A
    mid = (len(A)+1)//2
    left = A[:mid]
    right = A[mid:]
    return merge(A, merge_sort(left), merge_sort(right))

def merge(A, left, right):
    global count, num
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]: merged.append(left[l]); l+=1;
        else: merged.append(right[r]); r+=1;
    while l < len(left): merged.append(left[l]); l+=1
    while r < len(right): merged.append(right[r]); r+=1
    for i in range(len(A)):
        A[i] = merged[i]
        count -= 1
        if count == 0: num = merged[i]
    return A


N, K = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
count = K
num = -1
merge_sort(A)
print(num)