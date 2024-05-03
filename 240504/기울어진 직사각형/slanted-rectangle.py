n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, -1, 1]
dy = [-1, -1, 1, 1]
m = 0

for i in range(n):
    for j in range(n):
        k = 0
        cnt = 0
        nx, ny = i, j
        tmp = arr[i][j]

        while True:
            if 0 <= nx + dx[k] < n and 0 <= ny + dy[k] < n:
                nx += dx[k]
                ny += dy[k]
                if nx == i and ny == j:
                    break

                tmp += arr[nx][ny]
                cnt += 1

            else:
                if cnt == 0:
                    break
                cnt = 0
                k += 1
                if k == 4:
                    break

        if k >= 3:
            m = max(m, tmp)

print(m)