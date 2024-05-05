n = int(input())
arr = [0 for _ in range(2001)]
idx = 1000
for i in range(n):
    x, cmd = input().split()
    x = int(x)
    if cmd == 'L':
        for j in range(x+1):
            arr[idx] += 1
            idx -= 1
        idx += 1
    elif cmd == 'R':
        for j in range(x+1):
            arr[idx] += 1
            idx += 1
        idx -= 1

answer = 0

dots = []
for i in range(len(arr)):
    if arr[i] >= 2:
        dots.append(i)

stack = []
cnt = 0
for item in dots:
    if not stack:
        stack.append(item)
        cnt = 0
    else:
        prev_item = stack.pop()
        if item - prev_item == 1:
            stack.append(prev_item)
            stack.append(item)
            cnt += 1
        else:
            stack = []
            stack.append(item)
            answer += cnt
            cnt = 0

answer += cnt

print(answer)