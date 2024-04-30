n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

s = 0
for i in range(n-2):
    for j in range(n-2):
        x, y = i, j
        tmp = 0
        for l in range(3):
            for m in range(3):
                nx, ny = x + l, y + m
                if arr[nx][ny] == 1:
                    tmp += 1
        s = max(s, tmp)

print(s)