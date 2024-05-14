n, m = map(int, input().split())
arr_1, arr_2 = [0 for i in range(1000001)], [0 for i in range(1000001)]

time = 1
for i in range(n):
    direct, s = input().split()
    for j in range(int(s)):
        arr_1[time] = arr_1[time - 1] + (1 if direct == 'R' else -1)
        time += 1

time = 1
for i in range(m):
    direct, s = input().split()
    for j in range(int(s)):    
        arr_2[time] = arr_2[time - 1] + (1 if direct == 'R' else -1)
        time += 1

answer = -1

for t in range(1, 1000001):
    if arr_1[t] == arr_2[t]:
        answer = t
        break

print(answer)