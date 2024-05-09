n = int(input())

data = list(map(int, input().split()))
arr = [data[0]]

for i in range(1, n):
    tmp = max(arr[i-1] + data[i], data[i])
    arr.append(tmp)

print(max(arr))