class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}はルール違反だぞん！")
        self.name = name

    def screen_name(self,):
        return self.name.upper()


tanaka = UserName(name="tanaka")
# print(tanaka.name)
print(tanaka.screen_name())




