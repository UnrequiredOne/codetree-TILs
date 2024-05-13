n = int(input())

arr = [[0 for _ in range(201)] for _ in range(201)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(100+x1, 100+x2):
        for k in range(100+y1, 100+y2):
            arr[j][k] = 1

answer = 0
for i in range(201):
    answer += sum(arr[i])
print(answer)