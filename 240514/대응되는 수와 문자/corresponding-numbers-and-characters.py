n, m = map(int, input().split())
d = dict()

for i in range(n):
    data = input()
    if data not in d:
        d[data] = 0
    d[data] += 1

for i in range(m):
    data = input()
    if ord('a') <= ord(data) <= ord('z'):
        print(list(d.keys()).index(data) + 1)
    else:
        idx = int(data)
        print(list(d.keys())[idx-1])