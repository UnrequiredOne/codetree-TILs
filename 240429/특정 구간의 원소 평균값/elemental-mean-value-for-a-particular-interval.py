n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(n):
    for j in range(i+1, n+1):
        tmp = arr[i:j]
        avg = sum(tmp) / len(tmp)
        if avg in tmp:
            answer += 1

print(answer)