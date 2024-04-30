class player:
    def __init__(self, identity, level):
        self.id = identity
        self.level = level

    def print_info(self):
        print("user " + self.id, end=" ")
        print("lv " + self.level)


user, iid = input().split()
player_ = player("codetree", "10")
player_.print_info()

player_.id = user
player_.level = iid
player_.print_info()