arr = [[0 for _ in range(201)] for _ in range(201)]


n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x, y = x+100, y+100
    length = 8
    for j in range(x, x+length):
        for k in range(y, y+length):
            arr[j][k] = 1    

answer = 0
for i in range(201):
    answer += sum(arr[i])
print(answer)