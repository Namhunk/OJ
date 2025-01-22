import sys
input = sys.stdin.readline

# 첫째 줄부터 n-1개의 줄에 트리의 간선 정보를 출력한다. 트리의 정점은 0번부터 n-1번까지 이다

# n개의 노드, m개의 리프로 이루어진 트리를 만들기
n, m = map(int, input().strip().split())

prior = 0
for i in range(n):
    if m > 0:
        print(prior, i+1)
        m -= 1
    else:
        print(i, i+1)

"""
1. 리프 노드의 개수를 m개로 맞춰야 함
함수를 통과하며, 리프 노드를 만들어 주고 남은 리프 노드의 개수를 1개씩 제거
"""