import random
from sii3 import *
import unittest
a=[]
print(type(a))
class testClasters(unittest.TestCase):
    """tests for SII3"""

    def setUp(self):
        """начальная настройка
        """
        initPoint()
        initClasters()
        self.pointsDump = points

    def tearDown(self):
        '''complite test1'''
        '''проверка, что точки не изменили свое местопложение за время работаем'''
        if self.pointsDump == points:
            t = 1
        else:
            t = 0
        self.assertEqual(t, 1)

    def test_d(self):
        """растояние между 2 точками"""
        a = (1, 1)
        b = (1, 2)
        c = (10, 1)
        t1 = d(a, b)
        t2 = d(a, c)
        t3 = d(c, c)
        self.assertEqual(t1, 1)
        self.assertEqual(t2, 9)
        self.assertEqual(t3, 0)

    def test_D(self):
        """растоение между 2 кластерами"""
        cls1 = ((1, 1),)
        cls2 = ((1, 3), (5, 1))
        t = D(cls1, cls2)
        self.assertEqual(t, 4)


if __name__ == '__main__':
    unittest.main()