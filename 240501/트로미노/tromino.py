n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 1, 0, 2, 0]
dy = [0, 0, 1, 1, 0, 2]
pattern = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 4), (0, 3, 5)]
s = 0
for i in range(n):
    for j in range(m):
        for p in pattern:
            tmp = 0
            for k in p:
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    tmp += arr[nx][ny]
                else:
                    tmp = 0
                    break
            s = max(s, tmp)

print(s)