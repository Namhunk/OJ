import sys
input = sys.stdin.readline

def solve(code):
    print(code[::-1])


if __name__ == '__main__':
    while 1:
        # len(code) <= 500
        code = input().strip()
        if code == 'END': break
        solve(code)

"""

"""