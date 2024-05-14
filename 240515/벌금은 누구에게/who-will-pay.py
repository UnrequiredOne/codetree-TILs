n, m, k = map(int, input().split())
arr = [0 for _ in range(n + 1)]

stack = []

for i in range(m):
    student = int(input())
    arr[student] += 1
    if arr[student] >= k:
        stack.append(student)

answer = -1
if len(stack) > 0:
    answer = stack[0]

print(answer)