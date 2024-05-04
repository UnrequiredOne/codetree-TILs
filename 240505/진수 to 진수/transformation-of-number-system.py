a, b = map(int, input().split())
n = input()

num = 0
for i in range(0, len(n)):
    num = num * a + int(n[i])

answer = []
while num != 0:
    i = num % b
    num //= b
    answer.append(str(i))

print(''.join(answer[::-1]))