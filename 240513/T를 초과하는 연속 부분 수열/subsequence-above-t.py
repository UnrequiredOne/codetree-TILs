n, t = map(int, input().split())
arr = list(map(int, input().split()))

m, cnt = 0, 0
for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        m = max(m, cnt)
        cnt = 0

print(max(m, cnt))