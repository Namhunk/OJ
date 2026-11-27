import sys
import random, math
input = sys.stdin.readline

    
def solve():
    pass

def main():
    # 1 <= Q <= 200,000
    Q = int(input().strip())

    history = []
    stack = []
    for _ in range(Q):
        q = list(map(int, input().strip().split()))

        match q[0]:
            case 1:
                stack.append(q[1])
                history.append((q[0], q[1]))
            case 2:
                num = stack.pop()
                history.append((q[0], num))
            case 3:
                for _ in range(q[1]):
                    a, b = history.pop()
                    if a == 1:
                        stack.pop()
                    else:
                        stack.append(b)
            case 4:
                print(len(stack))
            case 5:
                print(stack[-1] if stack else -1)
                
if __name__ == '__main__':
    main()  

"""
1 i: 스택의 가장 위에 i를 집어넣음
2: 스택의 가장 위에 있는 값을 제거
3 j: 최근 j개의 1번 또는 2번 쿼리를 취소(취소할 수 있는 1번 2번 쿼리가 j개 이상인 경우만)
4: 스택의 크기 출력
5: 스택의 가장 위에 있는 값을 출력(비어있다면 -1)

"""