a, b = map(int, input().split())
n = input()

num = 0
for i in range(len(n) - 1 , -1, -1):
    num += pow(a, i)

answer = []
while num != 0:
    i = num % b
    num //= b
    answer.append(str(i))

print(''.join(answer[::-1]))