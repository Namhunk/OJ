import sys
input = sys.stdin.readline

def solve(G):
    arr = []
    i = 1
    while i < int(G**0.5)+1:
        if G % i == 0:
            A = G//i
            B = i
            num = (A+B)/2
            if A > B and num % 1 == 0:
                arr.append(int(num))
        i += 1
    
    if len(arr) == 0:
        print(-1)
    else:
        for i in arr[::-1]:
            print(i)

if __name__ == '__main__':
    # G (1 <= G <= 100,000)
    G = int(input().strip())
    solve(G)

"""
G = (현재 몸무게^2) - (마지막 몸무게^2)

가능한 현재 몸무게를 모두 출력, 없으면 -1

현재 몸무게가 A, 이전 몸무게가 B 일때
A^2 - B^2 = (A+B) x (A-B)

예제 1을 입력했을 때
나올 수 있는 경우는 (A+B), (A-B) = (15, 1), (5, 3) 2가지
결국 G를 소인수분해한 값들로 찾아야 함


"""