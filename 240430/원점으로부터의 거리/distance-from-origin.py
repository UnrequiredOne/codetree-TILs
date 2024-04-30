from functools import cmp_to_key

n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b, i+1))


def compare(x, y):
    return 1 if x[0] + x[1] > y[0] + y[1] or (x[0] + x[1] == y[0] + y[1] and x[2] > y[2]) else -1

arr.sort(key=cmp_to_key(compare))

for i in range(n):
    print(arr[i][2])