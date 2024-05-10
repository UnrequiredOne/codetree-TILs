n = int(input())
arr = []

for i in range(n):
    k, num = map(int, input().split())
    arr.append([k, num])

arr.sort(key=lambda x: x[1])

s = set()
i, j = 0, len(arr) - 1
while i != j:
    a, b = arr[i], arr[j]
    s.add(a[1] + b[1])
    if a[0] < b[0]:
        b[0] -= a[0]
        a[0] = 0
        i += 1
    elif a[0] > b[0]:
        a[0] -= b[0]
        b[0] = 0
        j -= 1
    else:
        a[0], b[0] = 0, 0
        i += 1
        j -= 1

print(max(s))