class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    

arr = []
for i in range(5):
    n, s = input().split()
    s = int(s)
    tmp = student(n, s)
    arr.append(tmp)

arr.sort(key= lambda x: x.score)
print(arr[0].name + " " + str(arr[0].score))