n, k, p, T = map(int, input().split())
max_T = 250
devs = [[0, 0] for _ in range(n + 1)]
devs[p] = [1, k]

time_table = [(0, 0) for _ in range(max_T+1)]
for i in range(T):
    t, x, y = map(int, input().split())
    time_table[t] = [x, y]

for x, y in time_table:
    if devs[x][0] and devs[x][1] >= 1:
        if devs[y][0] and devs[y][1] >= 1:
            devs[x][1] -= 1
            devs[y][1] -= 1
        elif devs[y][0]:
            devs[x][1] -= 1
        elif devs[y][0] == 0:
            devs[x][1] -= 1
            devs[y][0] = 1
            devs[y][1] = k
    elif devs[y][0] and devs[y][1] >= 1:
        if devs[x][0] == 0:
            devs[y][1] -= 1
            devs[x][0] = 1
            devs[x][1] = k
        elif devs[x][0]:
            devs[y][1] -= 1

for i in range(1, n+1):
    s, _ = devs[i]
    print(s, end="")