from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

q = deque()
q.append((0, 0))
flag = False


def is_valid_move(x, y):
    return 0 <= x < n and 0 <= y < m and arr[x][y] != 0 and visited[x][y] != 1


visited[0][0] = 1
while q:
    x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if next_x == n - 1 and next_y == m - 1:
            flag = True
            break
        if is_valid_move(next_x, next_y):
            q.append((next_x, next_y))
            visited[next_x][next_y] = 1

print(1 if flag else 0)