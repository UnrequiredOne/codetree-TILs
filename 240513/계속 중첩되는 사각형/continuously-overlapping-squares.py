n = int(input())

arr = [[0 for _ in range(201)] for _ in range(201)]

clr = 0
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = clr
    if clr == 0:
        clr = 1
    else:
        clr = 0

answer = 0
for i in range(201):
    answer += sum(arr[i])

print(answer)