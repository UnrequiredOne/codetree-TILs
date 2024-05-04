months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())
d = input()
t_d = day.index(d)

target = sum(months[i] for i in range(m1 + 1, m2)) + months[m1] - d1 + d2
answer, cnt = target // 7, target % 7

if cnt >= t_d:
    answer += 1

print(answer)