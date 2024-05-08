n = int(input())
dots = []
for i in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

s = []
for i in range(n):
    a, b = dots.pop(0)
    row = max(x for x, _ in dots) - min(x for x, _ in dots)
    col = max(y for _, y in dots) - min(y for _, y in dots)
    area = row * col
    dots.append((a, b))
    if area == 0:
        continue
    s.append(area)

if not s:
    answer = 0
else:
    answer = min(s)

print(answer)