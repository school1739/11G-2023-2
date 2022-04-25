# классы
class Player:
    def say(self, message):
        print(message)

    def sayShit(self):
        self.say('Shit!')

Ivanov = Player()
Petrov = Player()

Ivanov.say("I'm Ivanov")
Ivanov.sayShit()
Petrov.say("I'm Petrov")
Petrov.sayShit()

