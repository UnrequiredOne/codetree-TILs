n = int(input())
arr = [0 for _ in range(2001)]
idx = 1000
lines = []
for i in range(n):
    x, cmd = input().split()
    x = int(x)

    if cmd == 'L':
        x = x * -1
    elif cmd == 'R':
        x = x * 1

    start = idx
    idx += x
    end = idx
    if start > end:
        end, start = start, end

    lines.append((start, end))

answer = 0

for line in lines:
    for i in range(line[0], line[1]):
        arr[i] += 1

for i in range(2001):
    if arr[i] >= 2:
        answer += 1

print(answer)