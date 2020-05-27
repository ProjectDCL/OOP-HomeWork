class Figure():
    def __init__(self, name, coordinates, figureLength, figureWidth):
        self.name = name
        self.coordinates = coordinates
        self.figureLength = figureLength
        self.figureWidth = figureWidth


button = Figure("Кнопка", 40, 150, 200)

progressBar = Figure("Ползунок", 90, 100, 90)

figureGroup = [button, progressBar]

figureQuestion = input("Информация о какой фигуре Вас интересует? ")

for figureInfo in figureGroup:
    if figureQuestion == figureInfo.name:
        print("Искомая фигура:", figureInfo.name)
        print("Координаты левого верхнего угла:", figureInfo.coordinates)
        print("Длинна:", figureInfo.figureLength, "Ширина:", figureInfo.figureWidth)