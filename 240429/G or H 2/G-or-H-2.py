n = int(input())

arr = []
for i in range(n):
    l, t = input().split()
    l = int(l)
    t = 1 if t == 'G' else 2
    arr.append((l, t))

arr.sort()

s = 0
for i in range(n):
    for j in range(i+1, n+1):
        tmp = arr[i:j]
        cnt_1 = 0
        cnt_2 = 0
        for item in tmp:
            if item[1] == 1:
                cnt_1 += 1
            else:
                cnt_2 += 1
        if cnt_1 == 0 or cnt_2 == 0 or cnt_1 == cnt_2:
            s = max(s, tmp[-1][0] - tmp[0][0])

print(s)