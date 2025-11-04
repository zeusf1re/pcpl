class DisplayClass:
    """Дисплейный класс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Computer:
    """Компьютер"""
    def __init__(self, id, name, cost, class_id):
        self.id = id
        self.name = name
        self.cost = cost
        self.class_id = class_id

class CompClass:
    """'Компьютеры в классах' для связи многие-ко-многим"""
    def __init__(self, comp_id, class_id):
        self.comp_id = comp_id
        self.class_id = class_id

# Дисплейные классы
classes = [
    DisplayClass(1, 'Аудитория 501'),
    DisplayClass(2, 'Лаборатория сетей'),
    DisplayClass(3, 'Аудитория 333'),
]
# Компьютеры
computers = [
    Computer(1, 'HP Pavilion 15s', 95000, 1),
    Computer(2, 'MacBook Pro M4', 250000, 2),
    Computer(3, 'Dell XPS 13', 150000, 1),
    Computer(4, 'Asus ROG Zephyrus', 180000, 3),
    Computer(5, 'Lenovo IdeaPad s340s', 80000, 3),
]

# Связи многие-ко-многим
comps_classes = [
    CompClass(1, 1), CompClass(2, 2), CompClass(3, 1),
    CompClass(4, 3), CompClass(5, 3),
    # Добавим для примера, что MacBook есть и в 1-м классе
    CompClass(2, 1), # mac в 1 классе
]

def main():
    """Основная функция"""

    #  Д1 
    # Список компьютеров, название которых заканчивается на s, и их классов
    print('Задание Д1')
    one_to_many = [(comp.name, cls.name) 
                   for comp in computers 
                   for cls in classes 
                   if comp.class_id == cls.id and comp.name.endswith('s')]
    
    print(one_to_many)
    print()

    #  Д2
    # Список классов со средней стоимостью компьютеров в каждом, отсортированный по убыванию
    print('Задание Д2')
    res_d2 = []
    for cls in classes:
        class_comps = list(filter(lambda x: x.class_id == cls.id, computers))
        if len(class_comps) > 0:
            avg_cost = sum([comp.cost for comp in class_comps]) / len(class_comps) # сред
            res_d2.append((cls.name, int(avg_cost)))
            
    res_d2 = sorted(res_d2, key=lambda item: item[1], reverse=True) # по dec
    print(res_d2)
    print()
    
    # Д3
    # Список классов, начинающихся на 'А', и список компьютеров в них
    print('Задание Д3')
    
    # {id: Computer}
    comps_dict = {comp.id: comp for comp in computers} 
    # {id: DisplayClass}
    classes_dict = {cls.id: cls for cls in classes} 
    
    many_to_many = {}
    for cc in comps_classes:
        class_name = classes_dict[cc.class_id].name
        comp_name = comps_dict[cc.comp_id].name
        
        if class_name not in many_to_many:
            many_to_many[class_name] = []
        many_to_many[class_name].append(comp_name)

    # фильтр по названию с A
    res_d3 = {key: val for key, val in many_to_many.items() if key.startswith('А')}
    print(res_d3)


if __name__ == '__main__':
    main()
