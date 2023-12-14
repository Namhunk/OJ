import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

a_b, c_d = [], []
for i in range(n):
    for j in range(n):
        a_b.append(arr[i][0] + arr[j][1])
        c_d.append(arr[i][2] + arr[j][3])

a_b.sort()
c_d.sort()

def Two_Pointer():
    left, right = 0, n**2-1
    cnt = 0
    while left < n**2  and right > -1:
        SUM = a_b[left] + c_d[right]

        if SUM < 0: left += 1
        elif SUM > 0: right -= 1
        else:

            temp1, temp2 = left, right
            while temp1 < n**2 and a_b[left] == a_b[temp1]: temp1 += 1
            while temp2 > -1 and c_d[right] == c_d[temp2]: temp2 -= 1

            cnt += (temp1 - left) * (right - temp2)

            left, right = temp1, temp2
    
    return cnt

print(Two_Pointer())
