n = int(input())
arr = list(map(int, input().split()))
arr_idx = [(arr[i], i) for i in range(n)]
arr_idx.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    arr[arr_idx[i][1]] = i

for i in range(n):    
    print(arr[i] + 1, end=" ")