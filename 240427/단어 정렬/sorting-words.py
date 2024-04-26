n = int(input())

dt = [input() for _ in range(n)]
dt.sort()

for i in range(n):
    print(dt[i])