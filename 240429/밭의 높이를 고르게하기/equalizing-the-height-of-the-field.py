n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

s = [0 for _ in range(n-t)]

for i in range(n-t):
    for j in range(t):
        s[i] += abs(h - arr[i+j])

print(min(s))