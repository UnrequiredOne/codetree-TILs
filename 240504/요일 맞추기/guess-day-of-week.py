months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())

answer = 0
if m1 == m2:
    answer = d2 - d1
elif m1 < m2:
    answer = sum(months[m1+1:m2]) + months[m1] - d1 + d2
elif m1 > m2:
    answer = sum(months[m2+1:m1]) + months[m2] - d2 + d1

print(day[(answer % 7)])