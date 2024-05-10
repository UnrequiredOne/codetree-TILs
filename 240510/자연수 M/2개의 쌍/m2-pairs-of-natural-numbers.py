n = int(input())
arr = []

for i in range(n):
    k, num = map(int, input().split())
    for j in range(k):
        arr.append(num)

s = []
m = len(arr) // 2
for i in range(0, m):
    s.append(arr[i] + arr[len(arr) - 1 - i])

print(max(s))