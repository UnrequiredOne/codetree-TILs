from functools import cmp_to_key


class student:
    def __init__(self, n, a, b, c):
        self.name = n
        self.a = a
        self.b = b
        self.c = c
    
    def print_info(self):
        print(f"{self.name} {self.a} {self.b} {self.c}")


n = int(input())
arr = []
for i in range(n):
    name, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    s = student(name, a, b, c)
    arr.append(s)

def compare(x, y):
    return 1 if x.a + x.b + x.c > y.a + y.b + y.c else -1

arr.sort(key=cmp_to_key(compare))

for i in range(n):
    arr[i].print_info()