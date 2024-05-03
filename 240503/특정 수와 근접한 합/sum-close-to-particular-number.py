n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = sum(arr)
m = arr_sum * arr_sum

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        small_sum = arr[i] + arr[j]
        tmp = arr_sum - small_sum
        m = m if abs(s - m) < abs(s - tmp) else tmp

print(abs(s-m))