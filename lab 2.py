def check_input(message):
    inp = -1
    try:
        inp = int(input(message))
    except ValueError:
        print("Ошибка ввода! Пожалуйста, повторите!")
    return inp


def task1(n):
    count = 4
    i = 5
    while count != n:
        i += 2
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            count += 1
    if n == count:
        return i


def menu():
    choice = -1
    while choice != 0:
        print("\nВыберите:\n1.Task 1\n2.Task 2\n3.Task3\n4.Task4")
        while choice < 0 or choice > 4:
            choice = check_input("\nВаш выбор - ")
        if choice == 1:
            num = -1
            while num < 0:
                num = check_input("Пожалуйста, введите номер простого числа в последовательности простых чисел - ")
            if num < 4:
                number = num
            else:
                number = task1(num)
            print(f"Число под номером {num} равно {number}")
            choice = -1


menu()
