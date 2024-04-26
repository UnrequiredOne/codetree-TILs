n = int(input())

arr = [[0 for i in range(n)] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        arr[i][j] = tmp[j]

s = 0
for i in range(n):
    for j in range(n-2):
        for a in range(n):
            for b in range(n-2):
                if i == a and (j <= b <= j + 2 or b <= j <= b + 2):
                    continue
                s = max(s, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[a][b] + arr[a][b+1] + arr[a][b+2])

print(s)