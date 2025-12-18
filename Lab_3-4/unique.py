class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items) 
        self.used_elements = set() # set - это аналог std::unordered_set (хеш-таблица)
        self.ignore_case = kwargs.get('ignore_case', False) 

    def __iter__(self):
        return self # Стандартный boilerplate

    def __next__(self):
        while 1:
            current = next(self.items) 
            
            check_val = current
            if self.ignore_case:
                check_val = current.lower()
            
            if check_val in self.used_elements:
                continue

            self.used_elements.add(check_val)

            return current



data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print(*Unique(data))
