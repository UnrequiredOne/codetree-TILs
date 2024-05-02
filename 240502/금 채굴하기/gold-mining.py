n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

values = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        for k in range(n):
            cost, value = 2 * k * (k + 1) + 1, 0
            stack = [(i, j)]
            visited = []
            visited.append((i, j))

            while(stack):
                x, y = stack.pop(0)
                
                if arr[x][y] == 1:
                    value += 1

                for a in range(4):
                    nx, ny = x + dx[a], y + dy[a]
                    if 0 <= nx < n and 0 <= ny < n and abs(nx - i) + abs(ny - j) <= k and (nx, ny) not in visited:
                        stack.append((nx, ny))
                        visited.append((nx, ny))

            if cost < value * m:
                values.append(value)

if len(values) != 0:
    values.sort(reverse=True)

    print(values[0])
else:
    print(0)