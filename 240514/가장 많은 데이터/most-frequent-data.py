n = int(input())
d = dict()

for i in range(n):
    data = input()
    if data not in d:
        d[data] = 0
    d[data] += 1

print(max(d.values()))