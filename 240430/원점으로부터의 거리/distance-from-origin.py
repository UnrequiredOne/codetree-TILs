from functools import cmp_to_key

n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b, i+1))


def compare(x, y):
    return 1 if abs(x[0]) + abs(x[1]) > abs(y[0]) + abs(y[1]) or (abs(x[0]) + abs(x[1]) == abs(y[0]) + abs(y[1]) and x[2] < y[2]) else -1

arr.sort(key=cmp_to_key(compare))

for i in range(n):
    print(arr[i][2])