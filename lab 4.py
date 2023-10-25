class List:
    def __init__(self):
        self.data = []

    def add_element(self, el):
        self.data.append(el)

    def remove_last_element(self):
        self.data.pop()

    def reverse_list(self):
        self.data.reverse()

    def __len__(self):
        return len(self.data)

    def remove_element(self, value):
        try:
            self.data.remove(value)
        except ValueError:
            print("Нет элемента в списке!")


class Transport:
    price_per_km = 0
    speed = 0

    def __init__(self, price_per_km, speed):
        self.speed = speed
        self.price_per_km = price_per_km

    def method_of_transport(self):
        print("метод передвижения")


class Plane(Transport):
    def __init__(self, price_per_km, speed):
        super().__init__(price_per_km, speed)

    def method_of_transport(self):
        print("перелет на самолете")


class Train(Transport):
    def __init__(self, price_per_km, speed):
        super().__init__(price_per_km, speed)

    def method_of_transport(self):
        print("переезд на поезде")


class Auto(Transport):
    def __init__(self, price_per_km, speed):
        super().__init__(price_per_km, speed)

    def method_of_transport(self):
        print("перевозка на автомобиле")


class Room:
    height1 = 0
    length1 = 0
    height2 = 0
    length2 = 0

    @staticmethod
    def wallpaper(height1, length1, length2, square):
        return 2 * height1 * length1 + 2 * height1 * length2 - square


class Fruit:
    color = ""
    shape = ""
    taste = ""
    amount = 0

    def __init__(self, color, shape, taste):
        self.color = color
        self.shape = shape
        self.taste = taste
        Fruit.amount = Fruit.amount + 1

    def __del__(self):
        print("Объект удален")

    @staticmethod
    def opinion():
        print("Я думаю, фрукты очень вкусные")

    @classmethod
    def amount_of_fruits(cls):
        print("Всего фруктов: ", cls.amount)


def check_input(message):
    inp = -1
    try:
        inp = int(input(message))
    except ValueError:
        print("Ошибка ввода! Пожалуйста, повторите!")
    return inp


def menu():
    ll = List()
    choice1 = -1
    while choice1 != 0:
        print("\nВыберите:\n1.Task 1\n2.Task 2\n3.Task3\n4.Task4")
        while choice1 < 0 or choice1 > 4:
            choice1 = check_input("\nВаш выбор - ")
        if choice1 == 1:
            choice = -1
            while choice != 0:
                print("\nВыберите:\n1.Добавить элемент в конец списка\n2.Удалить последний элемент\n3.Перевернуть "
                      "список\n4.Вывести длину списка\n5.Удалить элемент со значением")
                while choice <= 0 or choice > 5:
                    choice = check_input("\nВаш выбор - ")
                if choice == 1:
                    el = check_input("Введите значение элемента")
                    ll.add_element(el)
                    choice = -1
                elif choice == 2:
                    if not ll:
                        print("Список пуст!")
                    else:
                        ll.remove_last_element()
                    choice = -1
                elif choice == 3:
                    ll.reverse_list()
                    choice = -1
                elif choice == 4:
                    if not ll:
                        print("Список пуст!")
                    else:
                        print(f"Длина списка - {ll.__len__()}")
                    choice = -1
                elif choice == 5:
                    if not ll:
                        print("Список пуст!")
                    else:
                        el = check_input("Введите значение элемента")
                        ll.remove_element(el)
                    choice = -1
            choice1 = -1
        elif choice1 == 2:
            plane = Plane(0.13, 340)
            train = Train(0.12, 160)
            auto = Auto(2.3, 120)
            with open("Transport.txt", "w") as transport:
                transport.write("Самолет" + str(plane.price_per_km) + str(plane.speed))
                transport.write("Поезд" + str(train.price_per_km) + str(train.speed))
                transport.write("Автомобиль" + str(auto.price_per_km) + str(auto.speed))
            choice_route = -1
            while choice_route != 0:
                print("Пожалуйста, выберите маршрут: \n1.Минск - Москва (675 км),\n2.Минск - Санкт-Петербург (692 "
                      "км)\n3.Минск - Баку (2242км)\n")
                while choice_route < 0 or choice_route > 3:
                    choice_route = check_input("\nВаш выбор - ")
                if choice_route == 1:
                    distance = 675
                elif choice_route == 2:
                    distance = 692
                else:
                    distance = 2242
                if choice_route != 0:
                    time = [plane.price_per_km / plane.speed, train.price_per_km / train.speed,
                            auto.price_per_km / auto.speed]
                    index_benefit = time.index(min(time))
                    if index_benefit == 0:
                        print(f"Самый выгодный вариант -")
                        plane.method_of_transport()
                        print(
                            f"время {round(distance / plane.speed, 2)} часа| стоимость {round(distance * plane.price_per_km, 2)} BYN")
                    elif index_benefit == 1:
                        print(f"Самый выгодный вариант -")
                        train.method_of_transport()
                        print(
                            f"время {round(distance / train.speed, 2)} часа| стоимость {round(distance * train.price_per_km, 2)} BYN")
                    elif index_benefit == 2:
                        print(f"Самый выгодный вариант -")
                        auto.method_of_transport()
                        print(
                            f"время {round(distance / auto.speed, 2)} часа| стоимость {round(distance * auto.price_per_km, 2)}BYN")
                    choice_route = 0
            choice1 = -1
        elif choice1 == 3:
            print("Пожалуйста, введите размер первой стены:")
            h1 = check_input("Высота - ")
            l1 = check_input("Длина - ")
            print("Пожалуйста, введите длину второй стены:")
            l2 = check_input("Длина - ")
            room = Room()
            door_h = check_input("Введите высоту дверного проема - ")
            door_l = check_input("Введите длину дверного проема - ")
            wind_ch = check_input("В комнате есть окна?(Да - 1)")
            square = door_l * door_h
            if wind_ch == 1:
                amount_wind = check_input("Введите количество: ")
                for i in range(amount_wind):
                    w_h = check_input("Введите высоту окна - ")
                    w_l = check_input("Введите длину окна - ")
                    square += w_h * w_l
                print(f"Площадь - {room.wallpaper(h1, l1, l2, square)}")
            else:
                print(f"Площадь - {room.wallpaper(h1, l1, l2, square)}")
            choice1 = -1
        elif choice1 == 4:
            apple = Fruit("red", "round", "sweet")
            orange = Fruit("orange", "round", "sweet")
            lemon = Fruit("yellow", "ellipse", "sour")
            print(f"Фрукт - Яблоко Цвет - {apple.color} Форма - {apple.shape} Вкус - {apple.taste}")
            print(f"Фрукт - Апельсин Цвет - {orange.color} Форма - {orange.shape} Вкус - {orange.taste}")
            print(f"Фрукт - Лимон Цвет - {lemon.color} Форма - {lemon.shape} Вкус - {lemon.taste}")
            Fruit.opinion()
            Fruit.amount_of_fruits()
            del apple
            choice1 = -1


menu()
