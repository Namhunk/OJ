import sys
input = sys.stdin.readline

"""
스타트링크 타워는 총 10^N개 층이 있다, 0층부터 10^N - 1 층으로 번호가 매겨져 있다.
층 번호를 숫자 N개로 표현한다. 숫자 N개로 층 번호를 표시할 수 없는 경우 앞에 0을 채운다.
숫자 1개를 표현하려면 전구 5 x 3 개가 필요하고, 이 전구를 세로 크기 5 가로크기 3인 격자 형태로 배치한다.
다음은 0부터 9까지 숫자를 나타낸 것이다. '#'는 불이 켜져있는 전구, '.'는 불이 꺼져있는 전구이다.

###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###

엘리베이터에 있는 층 번호 안내판의 상태가 주어진다. 안내판의 각 숫자는 불이 꺼져있는 전구 한 열로 구분되어 있다.
안내판의 일부 전구는 고장이 나서 항상 꺼져있는 상태이다. 꺼져있는 전구의 일부가 고장이 났다고 가정할 때,
현재 층 번호 안내판이 나타내고 있다고 볼 수 있는 모든 층 번호의 평균을 구해보자.

첫째 줄에 층 번호 안내판이 나타내고 있다고 가정할 수 있는 모든 층 번호의 평균을 출력한다. 
만약, 가능한 층 번호가 없는 경우 -1을 출력한다.

정답과의 절대/상대 오차는 10^-5까지 허용한다.
"""

lights = [[] for _ in range(10)] # 각 숫자별 형태를 저장할 배열
lights_string = """
###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###
"""

idx = 0
for i in range(1, len(lights_string), 4):
    lights[idx].append(lights_string[i: i+3])
    idx = (idx+1) % 10

# 각 숫자마다 전구에 불이 들어오면 안되는 위치를 저장
light_off = [set() for _ in range(10)]
for num in range(10):
    for i in range(5):
        for j in range(3):
            if lights[num][i][j] == '.':
                light_off[num].add((i, j))

# N (1 <= N <= 9)
N = int(input().strip())

idx = 0
# 각 안내판의 상태 N의 크기에 따라 나눔
arr = [[] for _ in range(N)]
for _ in range(5):
    row = input().strip()
    for i in range(1, N+1):
        arr[i-1].append(row[4*(i-1): 4*i-1])

maxFloor = (10**N)-1 # 최대 층 번호

curr_off = [set() for _ in range(N)] # 현재 안내판에 불이 꺼져있는 위치를 구함
for num in range(N):
    for i in range(5):
        for j in range(3):
            if arr[num][i][j] == '.':
                curr_off[num].add((i, j))

digit = [[] for _ in range(N)] # 각 위치마다 가능한 숫자들을 저장할 배열
for curr in range(len(curr_off)):
    for num in range(len(light_off)):
        if light_off[num] <= curr_off[curr]:
            digit[curr].append(num)

from math import prod
total_count = prod(len(d) for d in digit)

if total_count == 0:
    print(-1)
    exit()

ans = 0
for i in range(N):
    pos = digit[i]
    digit_sum = sum(pos)
    cnt = len(pos)
    mul = 10**(N-1-i)
    ans += (digit_sum * mul * total_count) // cnt

print(ans/total_count)

"""
5 x 3으로 각 숫자들을 나타냈을 때
해당 숫자로 바꿀 수 없는 위치들을 저장?
예를들어 1인 경우 arr[0][0], arr[0][1] 은 '#'가 있으면 안됨

"""
