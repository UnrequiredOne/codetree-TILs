n = int(input())
arr = []

for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x: (x[1], x[1] - x[0]))

cnt, end = 0, 0
for i in range(n):
    if end <= arr[i][0]:
        cnt += 1
        end = arr[i][1]

print(cnt)