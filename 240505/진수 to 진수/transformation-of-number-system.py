a, b = map(int, input().split())
n = input()

num = 0
for i in range(len(n) - 1 , -1, -1):
    num += pow(a, i)

answer = 0
while num != 0:
    i = num % b
    num //= b
    answer = answer * 10 + i

print(answer)