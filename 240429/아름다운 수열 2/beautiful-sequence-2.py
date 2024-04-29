n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_find = list(map(int, input().split()))

arr_find.sort()

answer = 0
for i in range(n-m+1):
    tmp = arr[i:i+m]
    tmp.sort()
    is_same = True
    for j in range(m):
        if tmp[j] == arr_find[j]:
            continue
        else:
            is_same = False
            break

    if is_same:
        answer += 1

print(answer)