weight_train = 0
axes = 0


def input_base_params():
    global weight_train
    weight_train = int(input("Введите вес поезда: "))
    count_wagons = int(input("Введите количество вагонов: "))
    calculate_count_axes(count_wagons)
    select_type_train()
    select_check_point()
    calculate_count_from_axes()


def calculate_count_axes(count_wagons):
    global axes
    axes = count_wagons * 4


def select_type_train():
    type_train = input("Порожний или Груженный поезд?: ")
    if type_train == "Порожний":
        print(weight_train * 0.55)
    else:
        print(weight_train * 0.33)


def select_check_point():
    check_point = input("Кедровка или Дальняк?: ")
    if check_point == "Кедровка":
        print(weight_train * 1.7 / 100)
    else:
        print(weight_train * 1.2 / 100)


def calculate_count_from_axes():
    wagon_3_5 = float(input("Сколько вагонов по 3.5?: ")) * 4
    wagon_7_0 = float(input("Сколько вагонов по 7.0?: ")) * 4
    wagon_7_5 = float(input("Сколько вагонов по 7.5?: ")) * 4
    wagon_8_5 = float(input("Сколько вагонов по 8.5?: ")) * 4

    summa = wagon_3_5 + wagon_7_0 + wagon_7_5 + wagon_8_5
    summa2 = (wagon_3_5 * 3.5) + (wagon_7_0 * 7.0) + (wagon_7_5 * 7.5) + (wagon_8_5 * 8.5)
    if axes == summa:
        print(round(summa2 / weight_train, 2))
    else:
        calculate_count_from_axes()


input_base_params()


