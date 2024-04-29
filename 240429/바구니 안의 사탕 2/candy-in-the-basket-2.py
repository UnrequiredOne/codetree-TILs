n, k = map(int, input().split())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((b, a))

arr.sort()

s = 0
for i in range(arr[0][0], arr[-1][0]):
    tmp = 0
    for item in arr:
        if i - k <= item[0] <= i + k:
            tmp += item[1]
    s = max(s, tmp)

print(s)