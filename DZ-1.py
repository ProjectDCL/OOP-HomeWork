# Практическая работа 1 — Выполнил Лавренчук Даниил. КН-21

def eat():
    print("Ням! Ням!")
    print("---------")


class Animal:
    def __init__(self, name, animalCategory):
        self.name = name
        self.animalCategory = animalCategory

    def displayStatus(self):
        print("Родилось животное! Его зовут:", self.name, )
        print("Это животное:", self.animalCategory)

    def makeNoise(self):
        print(self.name, "Говорит Гррр!")

    def setName(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name, animalCategory):
        super().__init__(name, animalCategory)

    def makeNoise(self):
        print(self.name, "Говорит Мяу!")


class Dog(Animal):
    def __init__(self, name, animalCategory):
        super().__init__(name, animalCategory)

    def makeNoise(self):
        print(self.name, "Говорит Гав!")

    def displayStatus(self):
        print("Родилось животное! Его зовут:", self.name, )
        print("Это животное: Собака")


# Default Animal Initialization
parrot = Animal("Пират", "Попугай")
parrot.displayStatus()
parrot.makeNoise()
eat()

# Cat Initialization
tisha = Cat("Тиша", "Кот")
tisha.displayStatus()
tisha.makeNoise()
eat()

# Dog Initialization
sebek = Dog("Себек", "Собака")
sebek.displayStatus()
sebek.makeNoise()
eat()

# Dog Initialization
muhtar = Dog("Мухтар", "Собака")
muhtar.displayStatus()
muhtar.makeNoise()
eat()