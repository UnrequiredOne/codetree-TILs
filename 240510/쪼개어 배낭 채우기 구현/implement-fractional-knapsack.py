n, m = map(int, input().split())

arr = []
for i in range(n):
    w, v = map(int, input().split())
    arr.append((w, v, v/w))

arr.sort(key=lambda x: x[2], reverse=True)
idx = 0
w, v = 0, 0

while m > 0:
    target = arr[idx]
    if m >= target[0]:
        m -= target[0]
        w += target[0]
        v += target[1]
        idx += 1
    else:
        w += m
        v += m * target[2]
        m = 0

print(f"{v:.3f}")