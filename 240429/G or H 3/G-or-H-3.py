n, k = map(int, input().split())

arr = []
for i in range(n):
    g, h = input().split()
    g = int(g)
    arr.append((g, h))

arr.sort()

s = 0
for i in range(n):
    tmp = 1 if arr[i][1] == 'G' else 2
    p = arr[i][0]
    for j in range(i + 1, n):
        item = arr[j]
        if item[0] - p <= k:
            tmp += 1 if item[1] == 'G' else 2
    s = max(s, tmp)

print(s)