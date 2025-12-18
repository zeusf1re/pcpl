def field(items, *args):
    assert len(args) > 0
    
    if len(args) == 1:
        key = args[0]
        for item in items:
            val = item.get(key)
            # Если значение не None, выдаем его
            if val is not None:
                yield val
    else:
        for item in items:
            dict = {}
            for characterics in args:
                if item.get(characterics):
                    dict[characterics] = item.get(characterics)

            if dict:
                yield dict

                
                
            

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

for i in field(goods, 'title'): print(i)
for i in field(goods, 'title', 'price'): print(i)
#tests
