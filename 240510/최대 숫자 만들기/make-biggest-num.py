from functools import cmp_to_key

n = int(input())

arr = []

for i in range(n):
    tmp = int(input())
    arr.append(tmp)

def compare(x, y):
    if int(str(x) + str(y)) > int(str(y) + str(x)):
        return -1
    else:
        return 1

arr.sort(key=cmp_to_key(compare))
answer = ''.join(str(i) for i in arr)

print(answer)