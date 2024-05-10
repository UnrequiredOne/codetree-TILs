c, n = map(int, input().split())
redstones = []
blackstones = []

for i in range(c):
    redstones.append(int(input()))
redstones.sort(reverse=True)

for i in range(n):
    a, b = map(int, input().split())
    blackstones.append((a, b))
blackstones.sort(key=lambda x: -x[1])

answer = 0
i, j = 0, 0
while i < c and j < n:
    r = redstones[i]
    b = blackstones[j]
    if b[0] <= r <= b[1]:
        answer += 1
        i += 1
        j += 1
    elif b[0] > r:
        j += 1
    elif b[1] < r:
        i += 1

print(answer)