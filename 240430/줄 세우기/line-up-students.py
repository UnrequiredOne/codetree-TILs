class student:
    def __init__(self, h, w, n):
        self.h = h
        self.w = w
        self.n = n
    
    def print_info(self):
        print(f"{self.h} {self.w} {self.n}")

n = int(input())

arr = []
for i in range(n):
    h, w = map(int, input().split())
    s = student(h, w, i+1)
    arr.append(s)

arr.sort(key=lambda x: (-x.h, -x.w, -x.n))

for i in range(n):
    arr[i].print_info()