A, B, x, y = map(int, input().split())

A, B = (A, B) if A < B else (B, A)
x, y =(x, y) if x < y else (y, x)

length = min(B - A, abs(A-x) + abs(B-y))

print(length)