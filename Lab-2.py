# Лабораторная работа 2
class Train():
    def __init__(self, name, point, time, seats):
        self.name = name
        self.point = point
        self.time = time
        self.seats = seats


train1 = Train("Одесса-Киев", "Киев", 16.20, True)
train2 = Train("Харьков-Киев", "Киев", 12.30, True)
train3 = Train("Бровары-Киев", "Киев", 22.15, False)
train4 = Train("Львов-Харьков", "Харьков", 11.48, True)
train5 = Train("Харьков-Днепропетровск", "Днепропетровск", 19.48, False)

trainArray = [train1, train2, train3, train4, train5]

point = input("Введите пункт назначения: ")
for trainGroup in trainArray:
    if point == trainGroup.point:
        print("Найдены поезда:", trainGroup.name)
        seats = trainGroup.seats
    if int(seats) == int(True):
        print("На рейсе", trainGroup.name, "есть свободные места!")

time = input("Введите время, после которого необходимо отправиться (Например 16.30): ")
for trainGroup in trainArray:
    if int(time) <= trainGroup.time:
        print("Найдены поезда:", trainGroup.name, "Их время отправления:", trainGroup.time)
