cook_book = {}
with open('text.txt', encoding='utf8') as f:
    name = f.readline().strip()
    while name != '':
        cook_book[name] = []
        for _ in range(int(f.readline().strip())):
            indigs = f.readline().strip().split('|')
            cook_book[name] += [{'ingredient_name': indigs[0].strip(),
                                 'quantity': int(indigs[1].strip()),
                                 'measure': indigs[2].strip()}]
        f.readline()
        name = f.readline().strip()

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    elements = {}
    for dish in dishes:
        for stats in cook_book[dish]:
            if stats['ingredient_name'] in elements:
                elements[stats['ingredient_name']]['quantity'] += stats['quantity']*person_count
            else:
                elements[stats['ingredient_name']] = {'measure': stats['measure'],
                                                      'quantity': stats['quantity']*person_count}

    return elements

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


