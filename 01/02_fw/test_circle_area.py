import unittest
from circle import circle_area
from math import pi

# Создаем класс для тестирования ф-ии, который
# наследуется от класса TestCase
class TestCircleArea(unittest.TestCase):

    # assertEqual - ф-ия, которая отслеживает равенство
    def test_area(self):
        self.assertEqual(circle_area(3), pi*3**2)
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.5), pi*2.5**2)

    # Проверим, выбрасывается ли исключение для отрицательных радиусов
    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(ValueError, circle_area, -1)

    # Проверим, выбрасывается ли исключение о несовместимости типов
    def test_types(self):
        self.assertRaises(TypeError, circle_area, 5+2j)
        self.assertRaises(TypeError, circle_area, 'five')
        self.assertRaises(TypeError, circle_area, [16, 22])
        self.assertRaises(TypeError, circle_area, [42])
        self.assertRaises(TypeError, circle_area, True) 

if __name__ == '__main__':
    unittest.main() 