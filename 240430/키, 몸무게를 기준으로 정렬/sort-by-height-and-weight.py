class student:
    def __init__(self, n, ki, kg):
        self.name = n
        self.ki = ki
        self.kg = kg
    
    def print_info(self):
        print(f"{self.name} {self.ki} {self.kg}")


n = int(input())
arr = []
for i in range(n):
    name, ki, kg = input().split()
    s = student(name, int(ki), int(kg))
    arr.append(s)

arr.sort(key=lambda x: (x.ki, -x.kg))
for i in range(n):
    arr[i].print_info()