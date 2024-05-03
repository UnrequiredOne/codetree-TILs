n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = sum(arr)
m = arr_sum

for i in range(n-1):
    for j in range(i+1, n):
        if i == j:
            continue

        small_sum = arr[i] + arr[j]
        tmp = arr_sum - small_sum
        m = m if abs(s - m) < abs(s - tmp) else tmp

print(abs(s-m))