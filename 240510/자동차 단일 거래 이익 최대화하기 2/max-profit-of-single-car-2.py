n = int(input())
arr = list(map(int, input().split()))

ben = [0 for _ in range(n)]
for i in range(n - 1):
    ben[i] = max(arr[i + 1:]) - arr[i]

print(max(ben))