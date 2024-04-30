class bomb:
    def __init__(self, code, color, t):
        self.code = code
        self.color = color
        self.t = t

    def print_info(self):
        print("code : " + self.code)
        print("color : " + self.color)
        print("second : " + str(self.t))


a, b, c = input().split()
D = bomb(a, b, c)
D.print_info()