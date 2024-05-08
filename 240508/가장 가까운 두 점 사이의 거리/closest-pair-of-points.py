n = int(input())

dots = []
for i in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

s = []
for i in range(n-1):
    for j in range(i+1, n):
        tmp = (dots[i][0] - dots[j][0], dots[i][1] - dots[j][1])
        dist = tmp[0]**2 + tmp[1]**2
        s.append(dist)

print(min(s))