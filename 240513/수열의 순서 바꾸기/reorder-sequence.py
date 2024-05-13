n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        answer = i + 1
        break
print(answer)