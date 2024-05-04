n = input()
length = len(n)

num = 0
for i in range(length):
    num = num * 2 + int(n[i])

print(num)