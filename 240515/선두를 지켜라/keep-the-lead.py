n, m = map(int, input().split())
max_t = 1000000

a = [0 for _ in range(max_t + 1)]
b = [0 for _ in range(max_t + 1)]

time = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a[time] = a[time - 1] + v
        time += 1

time = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b[time] = b[time - 1] + v
        time += 1

answer = 0
lead = 0 if a[1] > b[1] else 1
for i in range(1, time):
    if lead == 0 and a[i] < b[i]:
        answer += 1
        lead = 1
    elif lead == 1 and a[i] > b[i]:
        answer += 1
        lead = 0  

print(answer)