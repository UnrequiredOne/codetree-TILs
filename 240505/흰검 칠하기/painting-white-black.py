n = int(input())
arr = [[0, 0, ''] for _ in range(200001)]
idx = 100000

for i in range(n):
    x, cmd = input().split()
    x = int(x)
    if cmd == 'L':
        for j in range(x):
            arr[idx][0] += 1
            arr[idx][2] = cmd
            idx -= 1
        idx += 1
    elif cmd == 'R':
        for j in range(x):
            arr[idx][1] += 1
            arr[idx][2] = cmd
            idx += 1
        idx -= 1

w, g, b = 0, 0, 0
for item in arr:
    if item[0] >= 2 and item[1] >= 2:
        g += 1
    elif item[2] == 'L':
        w += 1
    elif item[2] == 'R':
        b += 1
    else:
        continue

print(w, b, g)