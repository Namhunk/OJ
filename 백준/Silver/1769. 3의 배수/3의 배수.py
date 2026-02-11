import sys
input = sys.stdin.readline

"""
문자열 X가 주어졌을 때 
각 자리수를 더한 값을 Y[1]이라고 함 X = 123인 경우 Y = 7
X가 주어졌을때 Y의 자릿수가 1개가 될때 까지 수행을 하고 그떄의 숫자가 3의 배수인지 확인

출력
1. 변환 과정을 몇 번 거쳤는지
2. 3의 배수인지 YES or NO
"""

X = input().strip()

cnt = 0
while len(X) > 1:
    SUM = 0
    for i in X:
        SUM += int(i)
    
    X = str(SUM)
    cnt += 1

print(cnt)
print('YES' if int(X) % 3 == 0 else 'NO')