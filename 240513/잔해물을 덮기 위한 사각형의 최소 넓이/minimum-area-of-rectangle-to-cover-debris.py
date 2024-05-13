arr = [[0 for _ in range(2001)] for _ in range(2001)]

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000

_x1, _y1, _x2, _y2 = map(int, input().split())
_x1, _y1, _x2, _y2 = _x1 + 1000, _y1 + 1000, _x2 + 1000, _y2 + 1000

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 1

for i in range(_x1, _x2):
    for j in range(_y1, _y2):
        arr[i][j] = 0

min_x, min_y, max_x, max_y = 2001, 2001, 0, 0
for i in range(x1, x2):
    for j in range(y1, y2):
        if arr[i][j] == 1:
            if min_x > i:
                min_x = i
            if min_y > j:
                min_y = j
            if max_x < i:
                max_x = i
            if max_y < j:
                max_y = j

answer = (max_x - min_x + 1) * (max_y - min_y + 1) if (max_x - min_x + 1) > 0 and (max_y - min_y + 1) else 0
print(answer)