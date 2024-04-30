class student:
    def __init__(self, name, ki, kg):
        self.name = name
        self.ki = ki
        self.kg = kg
    
    def print_info(self):
        print(f"{self.name} {self.ki} {self.kg}")


n = 5
arr = []

for i in range(n):
    name, ki, kg = input().split()
    s = student(name, int(ki), float(kg))
    arr.append(s)

arr.sort(key=lambda x:(x.name, -x.ki))
print("name")
for i in range(n):
    arr[i].print_info()

print()
print("height")
arr.sort(key=lambda x:(-x.ki))
for i in range(n):
    arr[i].print_info()