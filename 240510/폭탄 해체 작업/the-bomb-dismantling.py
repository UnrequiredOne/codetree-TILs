n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda x: x[1])

score = {}
for i in range(n):
    if arr[i][1] not in score:
        score[arr[i][1]] = 0
    score[arr[i][1]] = max(score[arr[i][1]], arr[i][0])

s = sum(score.values())
print(s)