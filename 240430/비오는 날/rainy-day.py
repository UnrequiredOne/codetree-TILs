class info:
    def __init__(self, t, d, s):
        self.t = t
        self.d = d
        self.s = s

    def print_info(self):
        print(f"{self.t} {self.d} {self.s}")


n = int(input())
arr = []
for i in range(n):
    t, d, s = input().split()
    state = info(t, d, s)
    arr.append(state)

arr.sort(key=lambda x: x.t)
for i in range(n):
    if arr[i].s == "Rain":
        arr[i].print_info()
        break