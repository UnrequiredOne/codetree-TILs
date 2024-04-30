n = int(input())
arr = []
for i in range(n):
    h, w = map(int, input().split())
    arr.append((h, w, i))

arr.sort(key=lambda x: (x[0], -x[1], x[2]))

for i in range(n):
    print(f"{arr[i][0]} {arr[i][1]} {arr[i][2] + 1}")