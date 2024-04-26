n, m = map(int, input().split())
arr = []
for i in range(n):
    tmp = input()
    arr.append(tmp)

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def is_valid_block(n, m, i, j):
    return 0 <= i < n and 0 <= j < m

answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            for k in range(8):
                nx, ny = i, j
                is_lee = True
                for l in range(2):
                    nx += dx[k]
                    ny += dy[k]
                    if is_valid_block(n, m, nx, ny) and arr[nx][ny] == 'E':
                        continue
                    else:
                        is_lee = False
                        break
                if is_lee:
                    answer += 1
                    
print(answer)