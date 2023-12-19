import sys

# 규칙을 유추한 뒤 별 찍기
def make_star(star):
    L = len(star)
    for i in range(L):
        # 공백을 사이에 두고 현재 행과 같은 모양의 별 2개 추가
        star.append(star[i] + ' ' + star[i])
        # 현재 행 양옆 공백 추가
        star[i] = (' '*L + star[i] + ' '*L)

# N이 가장 작을때 형태
star = ['  *  ', ' * * ', '*****']

# N입력 (3 <= N <= 3 x 2^10)
N = int(sys.stdin.readline().strip())
N //= 3 # star 배열의 반복 횟수

K = 0
while N > 1: # N이 1보다 큰 동안
    N //= 2
    K += 1

for i in range(K):
    make_star(star)
    
for i in star:
    print(i)