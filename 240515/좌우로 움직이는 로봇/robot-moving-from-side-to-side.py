max_t = 1000000

n, m = map(int , input().split())

a = [0 for _ in range(max_t + 1)]
b = [0 for _ in range(max_t + 1)]

time_a = 1
for i in range(n):
    t, d = input().split()
    d = 1 if d == 'R' else -1
    for j in range(int(t)):
        a[time_a] = a[time_a - 1] + d
        time_a += 1

time_b = 1
for i in range(m):
    t, d = input().split()
    d = 1 if d == 'R' else -1
    for j in range(int(t)):
        b[time_b] = b[time_b - 1] + d
        time_b += 1

if time_a < time_b:
    for i in range(time_a, time_b):
        a[i] = a[time_a - 1] 

elif time_a > time_b:
    for i in range(time_b, time_a):
        b[i] = b[time_b - 1] 

answer = 0
time = max(time_a, time_b)
for i in range(1, time):
    if a[i] == b[i] and a[i - 1] != b[i - 1]: 
        answer += 1

print(answer)