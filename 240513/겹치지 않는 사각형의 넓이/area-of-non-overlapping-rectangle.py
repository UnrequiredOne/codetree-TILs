arr = [[0 for _ in range(2001)] for _ in range(2001)]

for i in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(1000+x1, 1000+x2):
        for k in range(1000+y1, 1000+y2):
            arr[j][k] = 1

x1, y1, x2, y2 = map(int, input().split())
for i in range(1000+x1, 1000+x2):
    for j in  range(1000+y1, 1000+y2):
        arr[i][j] = 0

answer = 0
for i in range(2001):
    answer += sum(arr[i])
print(answer)