class Human():
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots movies")

    def speak(self):
        print(self.name, "says how are you?")

tom = Human("Tom", "actor")

tom.do_work()

tom.speak()

print("")

maria = Human("Maria", "tennis player")

maria.do_work()

maria.speak()