n = int(input())
arr = list(map(int, input().split()))

max_profit = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        profit = arr[j] - arr[i]
        if max_profit < profit:
            max_profit = profit

print(max_profit)