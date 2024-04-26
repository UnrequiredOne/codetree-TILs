n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = []
for i in range(n):
    tmp = arr[i] + arr[2 * n - 1 - i]
    m.append(tmp)

print(max(m))