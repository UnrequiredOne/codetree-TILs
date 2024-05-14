n, k = map(int, input().split())

arr = list(map(int, input().split()))
d = dict()
for item in arr:
    d[item] = 1

answer = 0
for item in d:
    if k - item in d and k != item * 2:
        answer += 1

print(answer // 2)