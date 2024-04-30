class product:
    def __init__(self, code, name):
        self.code = code
        self.name = name
    
    def set_info(self, code, name):
        self.code = code
        self.name = name
    
    def print_info(self):
        print("product " + str(self.code) + " is " + self.name)


p = product(50, "codetree")
p.print_info()

n, c = input().split()

p.set_info(c, n)
p.print_info()