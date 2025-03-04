import math

composition_weight = input("Введите вес поезда: ")
composition_weight1 = int(composition_weight)
number_of_axes = input("Введите число вагонов: ")
number_of_axes1 = int(number_of_axes) * 4
print(f"Количество осей = {number_of_axes1}")


# Выбор поезда
def train():
    composition_selection = input("Порожний или Груженый поезд?: ")
    result1 = int(composition_weight1) * 0.55
    result2 = int(composition_weight1) * 0.33

    if composition_selection == "Порожний":
        print("Требуемое нажатие колодок: ", math.ceil(result1))

    elif composition_selection == "Груженый":
        print("Требуемое нажатие колодок: ", math.ceil(result2))
    # Ответ округлять через math. ceil()


# Пункт куда поедет поезд
def hand_brakes_in_axles():
    next_point = input("Следующий пункт Кедровка или Дальняк?: ")
    result3 = float(composition_weight1) * 1.7 / 100
    result4 = float(composition_weight1) * 1.2 / 100

    if next_point == "Кедровка":
        print("Ручных тормозов в осях: ", math.ceil(result3))
    elif next_point == "Дальняк":
        print("Ручных тормозов в осях: ", math.ceil(result4))
    # Ответ округлять через math. ceil()


# Количество осей для n
def axles_35():
    axels_3_5 = input("Сколько вагонов по 3.5?: ")
    result5 = int(axels_3_5) * 4
    if axels_3_5 == 0:
        return
    else:
        print(f"Количество осей для 3.5 = {result5}")
        return result5


def axels_70():
    axels_7_0 = input("Сколько вагонов по 7.0?: ")
    result6 = int(axels_7_0) * 4
    if axels_7_0 == 0:
        return
    else:
        print(f"Количество осей для 7_0 = {result6}")
        return result6


def axels_75():
    axels_7_5 = input("Сколько вагонов по 7.5?: ")
    result7 = int(axels_7_5) * 4
    if axels_7_5 == 0:
        return
    else:
        print(f"Количество осей для 7.5 = {result7}")
        return result7


def axels_85():
    axels_8_5 = input("Сколько вагонов по 8.5?: ")
    result8 = int(axels_8_5) * 4
    if axels_8_5 == 0:
        return
    else:
        print(f"Количество осей для 8.5 = {result8}")
        return result8


# Сумма количество осей посчитанных в ручную
def total_number_of_axes():
    total_number_of_axes1 = axles_35() + axels_70() + axels_75() + axels_85()
    print("Всего осей посчитанных в ручную: ", total_number_of_axes1)
    return total_number_of_axes1


# Сравнение количество осей
def comparison():
    result = total_number_of_axes()
    if number_of_axes1 == result:
        print(f"Количество осей совпадает!: {number_of_axes1} = {result}")
    else:
        print(
            f"Количество осей не совпадает!: \nКоличество осей посчитанных программой: {number_of_axes1} не равно количеству осей посчитанных вручную!: {result}")
        return comparison()
        # Нужно чтоб заново с момента начинал, где надо пересчитать


# Тут нужно сделать, чтоб был скип при 0 и функции дальше выполнялись
def pressing_pads_1():
    pressing_pads1 = axles_35() * 3.5
    if pressing_pads1 == 0:
        print("По нулям!")
        return pressing_pads1
    else:
        print(f"Нажатие колодок для осей 3.5: {pressing_pads1}")
        return pressing_pads1


# Нажатие колодок для осей
def pressing_pads_2():
    pressing_pads2 = axels_70() * 7.0
    if pressing_pads2 == 0:
        print("По нулям!")
        return pressing_pads2
    else:
        print(f"Нажатие колодок для осей 7.0: {pressing_pads2}")
        return pressing_pads2


# Нажатие колодок для осей
def pressing_pads_3():
    pressing_pads3 = axels_75() * 7.5
    if pressing_pads3 == 0:
        print("По нулям!")
        return pressing_pads3
    else:
        print(f"Нажатие колодок для осей 7.5: {pressing_pads3}")
        return pressing_pads3


# Нажатие колодок для осей
def pressing_pads_4():
    pressing_pads4 = axels_85() * 8.5
    if pressing_pads4 == 0:
        print("По нулям!")
        return pressing_pads4
    else:
        print(f"Нажатие колодок для осей 8.5: {pressing_pads4}")
        return pressing_pads4


# сумма нажатия колодок
def pressing_pads_comparsion():
    pressing_pads_comparsion1 = pressing_pads_1() + pressing_pads_2() + pressing_pads_3() + pressing_pads_4()
    print(f"Сумма нажатия: {pressing_pads_comparsion1}")
    return pressing_pads_comparsion1


# достаточность нажатия
def sufficiency_of_pressing():
    sufficiency_of_pressing1 = pressing_pads_comparsion() / composition_weight1
    print(f"Достаточность нажатия: {round(sufficiency_of_pressing1, 2)}")


train()
hand_brakes_in_axles()
comparison()
sufficiency_of_pressing()

# train()
# hand_brakes_in_axles()
