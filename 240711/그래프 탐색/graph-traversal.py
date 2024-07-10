n, m = map(int, input().split())

arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1


def dfs(v):
    cnt = 1

    for i in range(1, len(arr[v])):
        if arr[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            cnt += dfs(i)

    return cnt


visited[1] = 1
print(dfs(1) - 1)