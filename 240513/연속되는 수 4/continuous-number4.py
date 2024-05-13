n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

m, cnt = 0, 1
for i in range(1, n):
    if arr[i - 1] < arr[i]:
        cnt += 1
    else:
        m = max(m, cnt)
        cnt = 1

print(max(m, cnt))