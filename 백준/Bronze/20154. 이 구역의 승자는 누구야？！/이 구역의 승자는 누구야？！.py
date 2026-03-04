import sys, string
input = sys.stdin.readline

def solve():
    global arr
    # 문자열 S (1 <= len(S) <= 1,000,000)
    S = list(input().strip())
    arr = [Convert[i] for i in S]

    while len(arr) > 1:
        temp = []
        for i in range(0, len(arr)-1, 2):
            SUM = (arr[i] + arr[i+1]) % 10
            temp.append(SUM)
        
        if len(arr) % 2 == 1:
            temp.append(arr[-1])
        
        arr = temp
        
    if arr[0] % 2 == 1:
        print("I'm a winner!")
    else:
        print("You're the winner?")

Alphabet = [i for i in string.ascii_uppercase]
Count    = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
Convert = {Alphabet[i]: Count[i] for i in range(len(Count))}
if __name__ == '__main__':
    solve()
    
"""
게임이 시작되면 알파벳 대문자로 이루어진 문자열이 주어짐
각 문자의 획수로 문자를 변환

홀수면 "I'm a winner!"
짝수면 "You're the winner?"
"""