import sys
input = sys.stdin.readline

# 첫째 줄에 길이가 n이고 3 825 123 056 546 413 051 이하의 소수로만 이루어진 등차수열을 출력한다
# 만약 그러한 등차수열이 없으면 대신 -1 을 출력한다
n = int(input().strip())

print(*[2]*n)
"""
길이가 n인 등차 수열, 공차가 0일때 n이 어떤 값이든 등차수열이 만들어짐
"""