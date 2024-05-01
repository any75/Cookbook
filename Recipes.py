

words_in_text = []
with open('Recipes.txt', 'r', encoding="utf-8") as f:
    for i in f:
        # print(i)
        words_in_text.append(i.strip().split('|'))
# print(words_in_text)
cook_book = {}
a = None
for l in words_in_text:
    # print(l)
    if len(l) == 1:
        # print(l)
        if not l[0].isdigit():
            if l[0] != '':
                a = l[0]
                cook_book[a] = []
    if len(l) == 3:
        cook_book[a].append({'ingredient_name': l[0], 'quantity': l[1], 'measure': l[2]})

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }

def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = {}
    if type(dishes) == type([]):
        for i in dishes:
            if i in cook_book:
                # print(cook_book[i])
                for j in cook_book[i]:
                    if j['ingredient_name'] in list_by_dishes:
                        list_by_dishes[j['ingredient_name']]['quantity'] += int(j['quantity']) * person_count
                    else:
                        list_by_dishes[j['ingredient_name']] = {'measure': j['measure'], 'quantity': int(j['quantity']) * person_count}
    print(list_by_dishes)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)






