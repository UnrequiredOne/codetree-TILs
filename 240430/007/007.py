class code:
    def __init__(self, code, location, t):
        self.code = code
        self.location = location
        self.t = t
    
    def print_(self):
        print("secret code : " + self.code)
        print("meeting point : " + self.location)
        print("time : " + self.t)


c, l, t = input().split()
agent = code(c, l, t)
agent.print_()