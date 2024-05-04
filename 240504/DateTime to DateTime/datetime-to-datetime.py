a, b, c = map(int, input().split())

answer = (a - 11) * 24 * 60 + (b - 11) * 60 + c - 11
if answer < 0:
    answer = -1

print(answer)