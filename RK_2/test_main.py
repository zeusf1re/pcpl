import unittest

from main import Computer, DisplayClass, CompClass, get_task_d1, get_task_d2, get_task_d3

class TestComputerTasks(unittest.TestCase):
    def setUp(self):
        self.classes = [
            DisplayClass(1, 'Аудитория 100'),
            DisplayClass(2, 'Буфет'),
            DisplayClass(3, 'Актовый зал'), # Класс без компьютеров (для проверки Д2)
        ]
        
        self.computers = [
            Computer(1, 'TestComp_s', 1000, 1),  # Заканчивается на 's', класс 1
            Computer(2, 'TestComp_x', 2000, 1),  # НЕ заканчивается на 's', класс 1
            Computer(3, 'SuperPC_s', 5000, 2),   # Заканчивается на 's', класс 2
        ]
        
        self.comps_classes = [
            CompClass(1, 1),
            CompClass(2, 1),
            CompClass(3, 2),
            CompClass(3, 1), # Компьютер 3 также связан с классом 1 (многие-ко-многим)
        ]

    def test_task_d1(self):
        """
        Тест Д1: Проверяет фильтрацию по окончанию имени на 's'
        """
        result = get_task_d1(self.computers, self.classes)
        
        
        expected = [
            ('TestComp_s', 'Аудитория 100'),
            ('SuperPC_s', 'Буфет')
        ]
        
        
        self.assertCountEqual(result, expected) # пофиг на порядок

    def test_task_d2(self):
        """
        Тест Д2: Проверяет расчет средней цены и сортировку
        """
        result = get_task_d2(self.computers, self.classes)
        
        
        expected = [
            ('Буфет', 5000),         # 1 место (5000 > 1500)
            ('Аудитория 100', 1500)  # 2 место
        ]
        
        self.assertEqual(result, expected)

    def test_task_d3(self):
        """
        Тест Д3: Проверяет связь многие-ко-многим и фильтр по 'А'
        """
        result = get_task_d3(self.computers, self.classes, self.comps_classes)
        
        # 'Аудитория 100' (начинается на А):
        # - Связана с комп 1, 2, 3 (через comps_classes)
        # 'Буфет' (НЕ начинается на А):
        # - Игнорируем
        # 'Актовый зал':
        # - Нет связей
        
        # В self.comps_classes у нас:
        # (1,1) -> TestComp_s в Ауд.100
        # (2,1) -> TestComp_x в Ауд.100
        # (3,2) -> SuperPC_s в Буфет (игнор)
        # (3,1) -> SuperPC_s в Ауд.100
        
        expected_keys = ['Аудитория 100']
        self.assertEqual(list(result.keys()), expected_keys)
        
        # Проверим состав списка для Аудитории 100
        expected_comps = ['TestComp_s', 'TestComp_x', 'SuperPC_s']
        self.assertCountEqual(result['Аудитория 100'], expected_comps)

if __name__ == '__main__':
    unittest.main()
