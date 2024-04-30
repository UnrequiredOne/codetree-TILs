class person:
    def __init__(self, n, c, l):
        self.name = n
        self.code = c
        self.location = l

    def print_info(self):
        print("name " + self.name)
        print("addr " + self.code)
        print("city " + self.location)


n = int(input())
arr = []

for i in range(n):
    name, addr, location = input().split()
    p = person(name, addr, location)
    arr.append(p)

arr.sort(key=lambda x: x.name)
arr[-1].print_info()