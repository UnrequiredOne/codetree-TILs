n, m = map(int, input().split())
arr = list(map(int, input().split()))
d = {}

for item in arr:
    if item not in d:
        d[item] = 0
    d[item] += 1

query = list(map(int, input().split()))
for q in query:
    if q not in d:
        print("0", end=" ")
    else:    
        print(d[q], end=" ")