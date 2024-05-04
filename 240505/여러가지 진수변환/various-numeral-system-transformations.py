n, b = map(int, input().split())

arr = []
while n != 0:
    a = n % 4
    arr.append(str(a))
    n = n // 4

answer = int("".join(arr[::-1]))
print(answer)