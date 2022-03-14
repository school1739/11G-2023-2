class Player:
    def say(self, message):
        print(message)
    def sayShit(self):
        self.say("Пошёл ты!")


Ivanov=Player()
Petrov=Player()
Ivanov.say("Дестиэль канон!")
Petrov.sayShit()