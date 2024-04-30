class person:
    def __init__(self, name, ki, kg):
        self.name = name
        self.ki = ki
        self.kg = kg

    def print_info(self):
        print(f"{self.name} {self.ki} {self.kg}")

n = int(input())
arr = []

for i in range(n):
    a, b, c = input().split()
    p = person(a, b , c)
    arr.append(p)

arr.sort(key=lambda x: x.ki)
for i in range(n):
    arr[i].print_info()