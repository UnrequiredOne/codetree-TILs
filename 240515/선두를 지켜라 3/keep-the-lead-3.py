max_t = 1000000

n, m = map(int, input().split())

a = [0 for _ in range(max_t + 1)]
b = [0 for _ in range(max_t + 1)]

time = 1
for i in range(n):
    v, t = map(int, input().split())
    for j in range(t):
        a[time] = a[time - 1] + v
        time += 1

time = 1
for i in range(m):
    v, t = map(int, input().split())
    for j in range(t):
        b[time] = b[time - 1] + v
        time += 1

answer = 1
lead = 1 if a[1] == b[1] else (0 if a[1] > b[1] else 2)
for i in range(1, time):
    now_lead = 0
    if a[i] > b[i]:
        now_lead = 0
    elif a[i] == b[i]:
        now_lead = 1
    else:
        now_lead = 2
    
    if lead != now_lead:
        answer += 1
        lead = now_lead

print(answer)