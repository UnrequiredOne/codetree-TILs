n, k = map(int, input().split())
d = dict()
arr = list(map(int, input().split()))
for i in range(n):
    data = arr[i]
    if data not in d:
        d[data] = 0
    d[data] += 1

arr = [(j, d[j]) for _, j in enumerate(d)]
arr.sort(key=lambda x: (-x[1], -x[0]))

for i in range(k):
    print(arr[i][0], end=" ")