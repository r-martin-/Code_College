class Mammal:
    mammal_population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Mammal.mammal_population += 1


class Dog(Mammal):
    dog_population = 0

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        Dog.dog_population += 1

    def __str__(self):
        return "{} is a dog - {}, {}".format(self.name, self.age, self.breed)

    def __repr__(self):
        return self.__str__()

    def bark(self, times):
        for i in range(times):
            print("Woof!")


class Cat(Mammal):
    cat_population = 0

    def __init__(self, name, age, lives):
        Mammal.__init__(self, name, age)
        self.lives = lives
        Cat.cat_population += 1

    def __str__(self):
        return "{} is a cat - {} {}".format(self.name, self.age, self.lives)

class Horse(Mammal):
    pass


# charlie = Dog("charlie", 3, "collie")
# print(charlie)
#
# tom = Cat("tom", 3, 9)
# print(tom)