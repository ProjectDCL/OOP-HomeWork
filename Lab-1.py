# Лабораторная работа 1 - 3 — Выполнил Лавренчук Даниил. КН-21
# Лабораторная работа 1

def delimiter():
    print("------------------")

class Train():
    def __init__(self, arrivalPoint, trainNumber, departureTime, freeSeatsReserved, freeSeatsCoupe):
        self.arrivalPoint = arrivalPoint
        self.trainNumber = trainNumber
        self.departureTime = departureTime
        self.freeSeatsReserved = freeSeatsReserved
        self.freeSeatsCoupe = freeSeatsCoupe
        self.freeSeatsTotal = self.freeSeatsReserved + self.freeSeatsCoupe


    def trainInformation(self):
        print("Добро пожаловать на официальный сайт Украинской Железной Дороги!")
        print("Показана информация о поезде номер:", self.trainNumber)
        print("Он отправится:", self.departureTime)
        print("Общее количество мест:", self.freeSeatsTotal, "Из них плацкартных:", self.freeSeatsReserved,
              "Также отображена информация о купейных местах, доступны к покупке:", self.freeSeatsCoupe)
        print("Спасибо за посещения нашего сайта! Будем рады видеть Вас на борту!")

# Train Info Initialization
train934 = Train("Киев", 934, "28 мая 18:34", 50, 61)
train934.trainInformation()
delimiter()