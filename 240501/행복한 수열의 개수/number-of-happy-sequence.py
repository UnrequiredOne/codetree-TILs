n, m = map(int, input().split())

arr = []
answer = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(n):
    prev_val = 0
    cnt = 0
    for j in range(n):
        if prev_val == arr[i][j]:
            cnt += 1
        else:
            if cnt >= m:
                answer += 1
                break
            prev_val = arr[i][j]
            cnt = 1
    
    if cnt >= m:
        answer += 1

for i in range(n):
    prev_val = 0
    cnt = 0
    for j in range(n):
        if prev_val == arr[j][i]:
            cnt += 1
        else:
            if cnt >= m:
                answer += 1
                break
            prev_val = arr[j][i]
            cnt = 1
    if cnt >= m:
        answer += 1

print(answer)