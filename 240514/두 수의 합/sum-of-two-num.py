n, k = map(int, input().split())

arr = list(map(int, input().split()))
d = dict()
for item in arr:
    if item not in d:
        d[item] = 0
    d[item] += 1

answer = 0
for item in d:
    if k - item in d and k != item * 2:
        answer += d[k - item] * d[item]
    elif k - item == item:
        answer += (d[item] - 1) * d[item]

print(answer // 2)