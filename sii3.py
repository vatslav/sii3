from tkinter import *
import random
from pprint import pprint
from math import sqrt
from copy import deepcopy
from PIL import Image,ImageDraw



def d(a, b):
    """нахождение растояния между 2 точками
    если а==б => вернуть 0"""
    if not isinstance(a, tuple):
        print(a,b,type(a), type(b))
        raise TypeError
    if a == b:
        return 0
    if not isinstance(a[0], float):
        a=a[0]
    if not isinstance(b[0],float):
        b=b[0]
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def D(claster1, claster2):
    '''нахождение растояния между 2 кластерами
    :param claster1: кластер точек
    :param claster2: кластер точек
    если а==б вернуть 0 (проверить это отеднльно)'''
    #проверка для отлова ошибок
    if not (isinstance(claster1, list) or isinstance(claster2, list)):
        print(claster1,claster2)
        raise TypeError

    if claster1 == claster2:
        return 0
    distance = 0
    #если нам дали на сравнение точку и лист, нужно точку засуноть в массив
    if not isinstance(claster1[0],tuple):
        claster1 = (tuple(claster1),)
    #аналогично
    if not isinstance(claster2[0],tuple):
        claster2 = (tuple(claster2),)

    #пробегаемся
    for point1 in claster1:
        for point2 in claster2:
            if not (isinstance(point1,tuple) or isinstance(point2,tuple)):
                print(point1, point2)
                print(claster1,clasters)
                print(len(claster1),len(claster2))
                raise TypeError
            checkDistance = d(point1, point2)
            if checkDistance > distance:
                distance = checkDistance
    return distance


points = []  # массив  кортежей из точек

pointsNumber = 10
dawnWall = 30
upWall = 650

clasters = []  # массив кластеров
distMx = []  # матрица растояний


def initPoint():
    '''инициализирует points случайнми точкми'''
    for n in range(pointsNumber):
        points.append((random.randint(dawnWall, upWall), random.randint(dawnWall, upWall)))


def initClasters():
    '''инициализирует clasters сначала 1 к 1'''
    for x in points:
        tmp = []
        tmp.append(list(x))
        clasters.append(tmp)
def printMx(mx):
    """красиво печатает матричу"""
    for x in mx:
        print(x)
def makeD():
    global distMx,clasters
    '''заполняет матрицу на основе текущего состояния кластеров'''
    lineIndex = 0
    distMx=[]

    for cls1 in clasters:
        distMx.append([])
        for cls2 in clasters:
            if not (isinstance(cls1, list) or isinstance(cls2, list)):
                print(cls1,cls2)
                raise TypeError
            dbuf = D(cls1, cls2)
            distMx[lineIndex].append(dbuf)

        lineIndex += 1
def step():
    """1 шаг алгоритма"""
    max = 0
    dx=0 # № первого кластера
    dy=0 # № второго кластера
    makeD()
    # находим наибольшее растоение между кластерами
    for y in range(len(distMx)):
        for x in range(len(distMx)):
            if distMx[y][x]>max:
                max = distMx[y][x]
                dy = x
                dx = y
    #print(dx,dy,max)
    #теперь нужно добавить все объекты первого ко второму, а первый удалить
    for iObj in clasters[dx]:
        clasters[dy].append(iObj)
    clasters.pop(dx)
    print('№Кластаера А=',dx,'№Кластера Б=',dy,'растоение=',max)
    print(clasters)
    return(dx,dy,max)



def stepHandler():

    while len(clasters)>2:
        yield step()
class windows:

    lineColor = "blue"
    bg = "lightblue"
    root=Tk()


    #oval = canv.create_oval(10,108,10,108,width=5,fill="black")
    width = 5 #толщина точки
    fill='black' #цвет заливки
    columnHeight = 25 #длина колонны
    coumnWidth = 3 #ширина колнны
    lineStart = 650 #линия с которой начинаем рисовать точки
    #storage = [[]]
    rFrame = Frame(root)
    lFrame = Frame(root)
    canv = Canvas(lFrame,width=700,height=700,bg="lightblue",cursor="pencil")


    stepIter = stepHandler()
    stepIter.__init__()
    def step(self):
        '''шаг прорисовки'''
        first,second,distance = self.stepIter.__next__()
        lineEnd = self.lineStart - self.columnHeight
        #self.canv.create_oval(400,650, 400,100,)
        print(self.storage)
        self.canv.create_oval(self.storage[first][0], lineEnd,self.storage[first][0],self.storage[first][1],
                              width=self.coumnWidth,fill=self.fill)

    def __init__(self, points):
        self.storage = deepcopy(points)
        #рисуем начальное расположение точек
        self.canv.create_oval(400,650, 400,100,width=self.width,fill=self.fill)
        #переносим точки на линию старта
        for nuber in range(len(self.storage)):
            tmp = list(self.storage[nuber])
            tmp[1] = self.lineStart
            self.storage[nuber] = tmp


        for point in self.storage:
            self.canv.create_oval(point[0],point[1],point[0],point[1],width=self.width,fill=self.fill)
        stepButton = Button(self.rFrame, text="Шаг",command=lambda :self.step())
        stepButton.grid()
        self.canv.grid(row=0,column=0)
        self.lFrame.grid(row=0,column=0)
        self.rFrame.grid(row=0,column=1)

        self.root.mainloop()



def main():
    '''основной цикл программы, работаем пока кластеров > 2'''

    initPoint()
    initClasters()
    windows(points)





def xmain():
    '''графический движок скрипта'''
    pass


if __name__ == '__main__':
    main()
