import math
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
        print("\nВыберите:\n1.Task 1\n2.Task 2\n3.Task3")
        while choice1 < 0 or choice1 > 3:
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
            distance = 0
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
                    time = [plane.price_per_km/plane.speed, train.price_per_km/train.speed, auto.price_per_km/auto.speed]
                    index_benefit = time.index(min(time))
                    if index_benefit == 0:
                        print(f"Самый выгодный вариант -")
                        plane.method_of_transport()
                        print(f"время {round(distance/plane.speed,2)} часа| стоимость {round(distance*plane.price_per_km, 2)} BYN")
                    elif index_benefit == 1:
                        print(f"Самый выгодный вариант -")
                        train.method_of_transport()
                        print(f"время {round(distance/train.speed, 2)} часа| стоимость {round(distance*train.price_per_km, 2)} BYN")
                    elif index_benefit == 2:
                        print(f"Самый выгодный вариант -")
                        auto.method_of_transport()
                        print(f"время {round(distance / auto.speed, 2)} часа| стоимость {round(distance * auto.price_per_km, 2)}BYN")
                    choice_route = 0
            choice1 = -1
        elif choice1 == 3:

            choice1 = -1


menu()
