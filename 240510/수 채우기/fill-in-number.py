n = int(input())

answer = 0
if n == 1 or n == 3:
    answer = -1

else:
    e, o = 0, 0
    if (n % 5) % 2 == 0:
        o = n // 5
        e = (n - 5 * o) // 2
    else:
        o = n // 5 - 1
        e = (n - 5 * o) // 2
    answer = e + o
print(answer)