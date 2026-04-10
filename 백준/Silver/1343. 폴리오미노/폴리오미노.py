import sys
input = sys.stdin.readline

def solve():
    # (len(board) <= 50)
    board = list(input().strip().split('.')) # '.' 을 기준으로 분할
    
    ans = []
    # 각 구간에 대해 검사
    for i in range(len(board)):
        # 2의 배수가 아니라면 -1 반환
        if len(board[i]) % 2 != 0: return -1
        # 1. 길이를 4로 나누었을때 몫만큼 Ax4 추가 나머지는 Bx2 추가
        # A가 앞에 올 수 있는 경우라면 A를 먼저 사용하는게 사전상 앞으로 옴
        A_size = len(board[i]) // 4
        B_size = len(board[i]) % 4
        
        AB = 'AAAA'*A_size + 'B'*B_size
        ans.append(AB)
    
    return '.'.join(ans)
        

if __name__ == '__main__':
    print(solve())

"""
. 와 X 로만 이루어진 보드판이 주어졌을 때
X를 모두 폴리오미노로 덮고 출력, 불가능하면 -1 출력

AAAA, BB 만 존재

X가 존재하는 구간의 길이가 2의 배수를 가져야 함


"""