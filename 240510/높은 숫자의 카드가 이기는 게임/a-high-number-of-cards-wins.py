n = int(input())

arr = [0 for i in range(1 + 2 * n)]

for i in range(n):
    arr[int(input())] = 1

cnt = 0
answer = 0
for i in range(1, 2*n + 1):
    if cnt != 0 and arr[i] == 0:
        cnt -= 1
        answer += 1
    else:
        cnt += 1

print(answer)