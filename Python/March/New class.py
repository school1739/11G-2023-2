class Human:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    # сеттер для имени где-то тут

    def get_info(self):
        print(f"Name: {self.__name}")

class Worker(Human):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def work(self):
        print(f"{self.name} works")
Rick = Human("Rick")
print(Rick.name)

Nick = Worker("Nick", )
print(Nick.name)