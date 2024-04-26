arr = []
n = int(input())
s = list(map(int, input().split()))

for i in range(n):
    arr.append(s[i])
    if i % 2 == 0:
        arr.sort()
        print(arr[i // 2], end=' ')