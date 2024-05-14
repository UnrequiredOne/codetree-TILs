n, m = map(int, input().split())
d = dict()

for i in range(n):
    data = input()
    d[data] = i

li = list(d.keys())
for i in range(m):
    data = input()
    if data.isdigit():
        print(li[int(data) - 1])
    else:
        print(d[data] + 1)