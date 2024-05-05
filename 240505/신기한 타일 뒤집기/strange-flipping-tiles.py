n = int(input())
arr = ['' for _ in range(200001)]
idx = 100000

for i in range(n):
    x, cmd = input().split()
    x = int(x)
    if cmd == 'L':
        for j in range(x):
            arr[idx] = cmd
            idx -= 1
        idx += 1
    elif cmd == 'R':
        for j in range(x):
            arr[idx] = cmd
            idx += 1
        idx -= 1

w, b = 0, 0
for item in arr:
    if item == '':
        continue
    elif item == 'L':
        w += 1
    elif item == 'R':
        b += 1

print(w, b)