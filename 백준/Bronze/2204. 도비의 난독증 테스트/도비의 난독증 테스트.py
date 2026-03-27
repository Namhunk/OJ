import sys
input = sys.stdin.readline

def solve(n):
    words = []

    for _ in range(n):
        word = input().strip()
        words.append((word.lower(), word))
    
    words.sort()
    print(words[0][1])
    

    

if __name__ == '__main__':
    while 1:
        # n (2 <= n <= 1,000)
        n = int(input().strip())
        if n == 0: break
        solve(n)

"""

"""