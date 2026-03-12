import sys
input = sys.stdin.readline

def solve():
    # 길이 50을 넘지 않는 단어 w, o, l, f로 만 구성되어 있음
    word = input().strip()

    wolf = ['w', 'o', 'l', 'f']
    curr = ''
    while len(curr) < len(word):
        size = len(curr)
        for i in range(1, 13):
            temp = ''
            for c in wolf:
                temp += c*i
            
            if temp == word[len(curr): len(curr) + len(temp)]:
                curr += temp
                break
        
        if len(curr) == size or curr != word[:len(curr)]: break
    
    print(int(curr == word))
            
if __name__ == '__main__':
    solve()

"""
1. 임의의 양의 정수 n에 대해서 w 가 n번 나오고, 그 다음에 o가 n번 그 다음에 l이 n번 그 다음에 f가 n번
나온 단어는 올바른 단어이다
2. 올바른 단어 두 개를 이은 단어도 올바른 단어이다.
3. 1번과 2번 조건으로 만들 수 있는 단어만 올바른 단어이다

순서도 w, o, l, f 순으로 나와야 함

4개의 단어에 대해
n = 1일때 길이 4
n = 2일때 길이 8

문자열의 길이는 4n으로 늘어남
문자의 최대 길이는 50 이하 이므로 n은 13보다 작은 숫자로 구성

4n <= 50 -> 13
모든 길이는 짝수

"""