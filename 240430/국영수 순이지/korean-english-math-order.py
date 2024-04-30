class student:
    def __init__(self, n, k, m, e):
        self.n = n
        self.k = k
        self.m = m
        self.e = e

    def print_info(self):
        print(f"{self.n} {self.k} {self.e} {self.m}")


n = int(input())
arr = []
for i in range(n):
    name, k, e, m = input().split()
    s = student(name, int(k), int(m), int(e))
    arr.append(s)

arr.sort(key=lambda x: (-x.k, -x.e, -x.m))
for i in range(n):
    arr[i].print_info()