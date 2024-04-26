n = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

arr_1.sort()
arr_2.sort()

is_same = True
for i in range(n):
    if arr_1[i] == arr_2[i]:
        continue
    else:
        is_same = False
        break

print('Yes' if is_same else 'No')