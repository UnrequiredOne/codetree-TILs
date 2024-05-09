n, k = map(int, input().split())

coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)
answer = 0
index = 0
while k > 0:
    if k < coins[index]:
        index += 1
    else:
        k -= coins[index]
        answer += 1

print(answer)