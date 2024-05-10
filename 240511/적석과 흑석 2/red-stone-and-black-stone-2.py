c, n = map(int, input().split())
redstones = []
blackstones = []

for i in range(c):
    redstones.append(int(input()))
redstones.sort()

for i in range(n):
    a, b = map(int, input().split())
    blackstones.append((a, b))
blackstones.sort(key=lambda x: x[0])

answer = 0
r_idx, b_idx = 0, 0

while r_idx < c and b_idx < n:
    r = redstones[r_idx]
    b = blackstones[b_idx]
    if b[0] <= r <= b[1]:
        answer += 1
        r_idx += 1
        b_idx += 1
    elif b[0] > r:
        r_idx += 1
    elif b[1] < r:
        b_idx += 1

print(answer)