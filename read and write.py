



def adding_a_recipe():
    """"Добавление рецепта"""
    with open('a.txt','a') as fo:
        name = input('введите название')
        quantity = int(input('введите количество'))

        fo.write(f'{name}\n')
        fo.write(f'{quantity}\n')
        _ = 0
        while _ != quantity:
            name_ingr = input('введите название ингридиента')
            quantiti_ingr = int(input('Введите количество ингридиента'))
            measure = input('Введите единицу измерения')
            fo.write(f'{name_ingr},{quantiti_ingr},{measure}\n')
            _ +=1

def reading_the_recipe():
    ''''Чтение рецептов в словарь'''
    with open('a.txt', 'r') as fo:
        cook_book_1 = {}
        for l in fo:
            name = l.strip()
            ing_quan = int(fo.readline().strip())

            my_list = []
            for i in range(ing_quan):
                ingr = fo.readline().split(',')
                ingridients = {'ingridients_name': ingr[0].strip(), 'quantity': ingr[1].strip(),
                               'measure': ingr[2].strip()}
                # print(ingr)
                my_list.append(ingridients)
                cook_book_1[name] = my_list
    # for item  in cook_book_1:
    # print(cook_book_1)
    return cook_book_1

def calculation_ingridients(dish_list,person_number):
    ''''расчет количества ингридиентов'''
    print(dish_list,person_number)

    with open('a.txt', 'r') as fo:

        cooc_b = {}

        for l in fo:
            name = l.strip()
            ing_quan = int(fo.readline().strip())
            # print(name, ing_quan)
            my_list = []

            for i in range(ing_quan):
                ingr = fo.readline().split(',')
                # print(ingr)
                ing_q = int(ingr[1])
                ing_q *= person_number
                if name in dish_list:
                    cooc_b[ingr[0]] = {'measure': ingr[2].strip(), 'quantity': ing_q}
        print(cooc_b)







while True:
    print('1 - добавление рецепта, 2 - чтение рецептов, 3 - расчет количества ингридиенотов, 0 - выход')
    user_input = int(input('сделайте выбор'))
    if user_input == 1:
        adding_a_recipe()
    if user_input == 2:
        print(reading_the_recipe())

    if user_input == 3:
        list_of_the_dish = []
        number_of_persons = 2
        print(reading_the_recipe().keys())
        while True:
            name_of_the_dish = input('введите наименования блюд/q - выход')
            if name_of_the_dish == 'q':
                break
            list_of_the_dish.append(name_of_the_dish)
        number_of_persons = int(input('введите количество персон'))
        calculation_ingridients(list_of_the_dish,number_of_persons)
    if user_input == 0:
        break



