import unittest 
from circle import circle_lenght
from math import pi

class TestCircleLenght(unittest.TestCase):

    # assertEqual - ф-ия, которая отслеживает равенство
    def test_area(self):
        self.assertEqual(circle_lenght(3), 2*pi*3)
        self.assertEqual(circle_lenght(1), 2*pi*1)
        self.assertEqual(circle_lenght(0), 0)
        self.assertEqual(circle_lenght(2.5), 2*pi*2.5)

    # Проверим, выбрасывается ли исключение для отрицательных радиусов
    def test_values(self):
        self.assertRaises(ValueError, circle_lenght, -2)
        self.assertRaises(ValueError, circle_lenght, -1)

    # Проверим, выбрасывается ли исключение о несовместимости типов
    def test_types(self):
        self.assertRaises(TypeError, circle_lenght, 5+2j)
        self.assertRaises(TypeError, circle_lenght, 'five')
        self.assertRaises(TypeError, circle_lenght, [16, 22])
        self.assertRaises(TypeError, circle_lenght, [42])
        self.assertRaises(TypeError, circle_lenght, True) 

if __name__ == '__main__':
    unittest.main() 