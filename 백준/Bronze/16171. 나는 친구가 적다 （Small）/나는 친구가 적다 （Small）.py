import sys
input = sys.stdin.readline

def solve():
    # S (1 <= |S| <= 100)
    S = list(input().strip())

    # K (1 <= |K| <= 100)
    K = list(input().strip())

    # 숫자를 제거한 문자열
    ORG = []
    for i in range(len(S)):
        if S[i].isdigit(): continue
        ORG.append(S[i])
    
    ans = 0
    # 숫자가 없는 문자열에서 일치 여부를 확인
    for i in range(len(ORG)-len(K)+1):
        if ORG[i: i+len(K)] == K:
            ans = 1
            break
    
    print(ans)

    
if __name__ == '__main__':
    solve()

"""
교과서는 a-z, A-Z, 0-9 로만 이루어짐
교과서에서 찾고자 하는 키워드의 존재 여부

1. 주어진 문자열에서 숫자만을 제거했을때 일치하는 부분이 있다면 O
2. 숫자만을 제거 했을때 일치하는 부분이 없다면 X
"""