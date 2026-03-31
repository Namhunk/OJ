import sys
input = sys.stdin.readline

def solve():
    S = input().rstrip('\n')

    ans = ''
    for c in S:
        if c == ' ' or c.isnumeric():
            ans += c
        else:
            idx = ord(c)

            if idx < 91:
                idx = (idx+13-65) % 26 + 65
            
            else:
                idx = (idx+13-97) % 26  + 97
            
            ans += chr(idx)
    
    print(ans)

if __name__ == '__main__':
    solve()

"""
ROT13은 영어 알파벳을 13글자씩 밀어서 만든다

"""