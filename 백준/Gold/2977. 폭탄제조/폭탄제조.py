N, M = map(int, input().split())
X = [0] * (100 + 10)
Y = [0] * (100 + 10)
Sm = [0] * (100 + 10)
Pm = [0] * (100 + 10)
Sv = [0] * (100 + 10)
Pv = [0] * (100 + 10)

for i in range(N):
    X[i], Y[i], Sm[i], Pm[i], Sv[i], Pv[i] = map(int, input().split())

def is_possible(num_food):
    cur_money = M
    for i in range(N):
        money_ = 1 << 30
        need = X[i] * num_food - Y[i]
        p_range = need // Sm[i]
        if need % Sm[i] > 0:
            p_range += 1
        for p in range(p_range + 1):
            left_need = need - p * Sm[i]
            q = 0 if left_need <= 0 else left_need // Sv[i]
            if left_need > 0 and left_need % Sv[i] > 0:
                q += 1
            money_ = min(money_, p * Pm[i] + q * Pv[i])
        cur_money -= money_
        if cur_money < 0:
            return False
    return False if cur_money < 0 else True

s = 0
e = max(M // Pm[0], M // Pv[0])

for i in range(M // Pm[0] + 1):
    left_money = M - Pm[0] * i
    j = left_money // Pv[0]
    ingredient = i * Sm[0] + j * Sv[0]
    e = max(e, (ingredient + Y[0]) // X[0])

sol = -1
while e >= s:
    mid = (e + s) // 2
    if is_possible(mid):
        s = mid + 1
        sol = mid
    else:
        e = mid - 1

print(sol)
