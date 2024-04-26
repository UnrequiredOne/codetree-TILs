a, b  = list(input()), list(input())
a.sort()
b.sort()

n = len(a)
is_same = True
if n == len(b):
    for i in range(n):
        if a[i] == b[i]:
            continue
        else:
            is_same = False
            break
else:
    is_same = False
    
print('Yes' if is_same else 'No')