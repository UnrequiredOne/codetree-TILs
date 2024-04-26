n, k, s = input().split()
n = int(n)
k = int(k)

dt = []
for i in range(n):
    tmp = input()
    is_same = True
    for j in range(len(s)):
        if s[j] == tmp[j]:
            continue
        else:
            is_same = False
            break
    if is_same:
        dt.append(tmp)

dt.sort()
print(dt[k - 1])