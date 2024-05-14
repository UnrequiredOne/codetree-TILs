n, m = map(int, input().split())
d = dict()

for i in range(n):
    data = input()
    if data not in d:
        d[data] = 0
    d[data] += 1

for i in range(m):
    data = input()
    if data.isdigit():
        print(list(d.keys())[int(data) - 1])
    else:
        print(list(d.keys()).index(data) + 1)