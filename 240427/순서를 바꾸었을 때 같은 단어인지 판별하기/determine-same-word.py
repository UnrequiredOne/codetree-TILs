a, b  = list(input()), list(input())
a.sort()
b.sort()

n = len(a)
is_same = True

for i in range(n):
    if a[i] == b[i]:
        continue
    else:
        is_same = False
        break

print('Yes' if is_same else 'No')