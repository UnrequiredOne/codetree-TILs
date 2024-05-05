n = int(input())
arr = [0 for _ in range(2001)]
idx = 1001
for i in range(n):
    x, cmd = input().split()
    x = int(x)
    if cmd == 'L':
        for j in range(x):
            arr[idx] += 1
            idx -= 1
    elif cmd == 'R':
        for j in range(x):
            arr[idx] += 1
            idx += 1

answer = 0

for item in arr:
    if item >= 2:
        answer += 1

print(answer)