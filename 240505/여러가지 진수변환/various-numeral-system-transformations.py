n, b = map(int, input().split())

arr = []
while n != 0:
    a = n % b
    arr.append(str(a))
    n = n // b

answer = int("".join(arr[::-1]))
print(answer)