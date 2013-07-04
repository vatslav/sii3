from tkinter import *
import random
from pprint import pprint
from math import sqrt
from copy import deepcopy


def d(a, b):
    """нахождение растояния между 2 точками
    если а==б => вернуть 0"""
    if not isinstance(a, tuple):
        print(a,b,type(a), type(b))
        raise TypeError
    if a == b:
        return 0
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
dawnWall = 0
upWall = 15

clasters = []  # массив кластеров
distMx = []  # матрица растояний


def initPoint():
    '''инициализирует points случайнми точкми'''
    for n in range(pointsNumber):
        points.append((random.randint(dawnWall, upWall), random.randint(dawnWall, upWall)))


def initClasters():
    '''инициализирует clasters сначала 1 к 1'''
    for x in points:
        clasters.append(list(x))
def printMx(mx):
    """красиво печатает матричу"""
    for x in mx:
        print(x)
def makeD():
    '''заполняет матрицу на основе текущего состояния кластеров'''
    lineIndex = 0


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
    """1 лаг алгоритма"""
    max = 0
    dx=0 # № первого кластера
    dy=0 # № второго кластера
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
    print(clasters)



def main():
    '''основной цикл программы, работаем пока кластеров > 2'''
    initPoint()
    initClasters()
    makeD()
    print(points)
    print(clasters)
    print()
    while len(clasters)>2:
        step()

    #print(clasters)
    #step()
    #print()
    #printMx(distMx)





def xmain():
    '''графический движок скрипта'''
    pass


if __name__ == '__main__':
    main()
