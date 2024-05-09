n = int(input())
arr = list(map(int, input().split()))

max_profit = 0
min_price = arr[0]

for i in range(1, n):
    profit = arr[i] - min_price
    
    if min_price > arr[i]:
        min_price = arr[i]

    if max_profit < profit:
        max_profit = profit

print(max_profit)