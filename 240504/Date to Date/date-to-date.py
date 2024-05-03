a, b, c, d = map(int, input().split())

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

answer = 0
if a == c:
    answer = d - b
else:
    for i in range(a+1, c):
        answer += months[i]
    answer += d + months[a] - b + 1

print(answer)