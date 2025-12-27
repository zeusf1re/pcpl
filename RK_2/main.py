import operator

class DisplayClass:
    """Display"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Computer:
    """Comp"""
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


classes = [
    DisplayClass(1, 'Аудитория 501'),
    DisplayClass(2, 'Лаборатория сетей'),
    DisplayClass(3, 'Аудитория 333'),
]

computers = [
    Computer(1, 'HP Pavilion 15s', 95000, 1),
    Computer(2, 'MacBook Pro M4', 250000, 2),
    Computer(3, 'Dell XPS 13', 150000, 1),
    Computer(4, 'Asus ROG Zephyrus', 180000, 3),
    Computer(5, 'Lenovo IdeaPad s340s', 80000, 3),
]

comps_classes = [
    CompClass(1, 1), CompClass(2, 2), CompClass(3, 1),
    CompClass(4, 3), CompClass(5, 3),
    CompClass(2, 1), # mac в 1 классе
]

def get_task_d1(computers, classes):
    """
    Список компьютеров, название которых заканчивается на 's', и их классов.
    Возвращает список кортежей (название_компа, название_класса).
    """
    return [
        (comp.name, cls.name)
        for comp in computers
        for cls in classes
        if comp.class_id == cls.id and comp.name.endswith('s')
    ]

def get_task_d2(computers, classes):
    """
    Список классов со средней стоимостью компьютеров, отсортированный по убыванию средней цены.
    Возвращает список кортежей (название_класса, средняя_цена).
    """
    res_d2 = []
    for cls in classes:
        # Фильтруем компы текущего класса
        class_comps = list(filter(lambda x: x.class_id == cls.id, computers))
        
        if len(class_comps) > 0:
            # Считаем среднюю цену
            avg_cost = sum([comp.cost for comp in class_comps]) / len(class_comps)
            res_d2.append((cls.name, int(avg_cost)))
            
    # Сортировка по убыванию цены
    return sorted(res_d2, key=lambda item: item[1], reverse=True)

def get_task_d3(computers, classes, comps_classes):
    """
    Список классов, начинающихся на 'А', и список компьютеров в них (многие-ко-многим).
    Возвращает словарь {класс: [список компьютеров]}.
    """
    # {id: Computer}
    comps_dict = {comp.id: comp for comp in computers}
    # {id: DisplayClass}
    classes_dict = {cls.id: cls for cls in classes}
    
    many_to_many = {}
    
    for cc in comps_classes:
        cls_obj = classes_dict.get(cc.class_id)
        comp_obj = comps_dict.get(cc.comp_id)
        
        # Защита от битых ссылок
        if not cls_obj or not comp_obj:
            continue

        class_name = cls_obj.name
        comp_name = comp_obj.name
        
        if class_name not in many_to_many:
            many_to_many[class_name] = []
        many_to_many[class_name].append(comp_name)
        
    # Фильтр по названию класса (начинается на 'А')
    return {key: val for key, val in many_to_many.items() if key.startswith('А')}

def main():
    print('Задание Д1')
    print(get_task_d1(computers, classes))
    print()
    
    print('Задание Д2')
    print(get_task_d2(computers, classes))
    print()
    
    print('Задание Д3')
    print(get_task_d3(computers, classes, comps_classes))

if __name__ == '__main__':
    main()
