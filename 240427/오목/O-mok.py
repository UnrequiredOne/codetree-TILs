n = 19

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]


winner = 0
final = (0, 0)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            continue
        elif arr[i][j] in (1, 2):
            for k in range(8):
                cnt = 1
                nx, ny = i, j
                for l in range(4):
                    nx += dx[k]
                    ny += dy[k]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[i][j]:
                        cnt += 1
                    else:
                        break
                if cnt == 5:
                    winner = arr[i][j]
                    final = (nx - 2 * dx[k], ny - 2 * dy[k])
                    break

        if winner != 0:
            break
    if winner != 0:
        break

print(winner)
print(final[0] + 1, final[1] + 1)