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


def task2(smth):
    if type(smth, list):
        count = 0
        max_int = 0
        numbers = False
        for el in smth:
            if type(el, int):
                numbers = True
                if el % 2 == 0:
                    count += 1
                if el > max_int:
                    max_int = el
                if el < 0:
                    smth.remove(el)
        if numbers:
            print(f"Максимальное число - {max_int}")
            if count == 0:
                print("Нет четных чисел!")
            else:
                print(f"Количество четных чисел - {count}")
            print(f"Новый список: {smth}")
        else:
            print("Список не содержит чисел!")
    elif type(smth, dict):
        sorted_dict = sorted(smth.items(), key=lambda v: v[1], reverse=True)
        print(f"Отсортированный в обратном порядке по значениям словарь: {sorted_dict}\n")
    elif type(smth, int):
        rev_num = str(smth)
        print(f"Перевернутое число - {rev_num[0:0:-1]}")
    elif type(smth, str):
        d = {}
        for el in smth:
            if el not in d:
                d[el] = f'{smth.count("el")}'
        print(d)
    else:
        print("Не подходящий тип данных!")


def task3(m):
    if type(m, list):
        for i in m:
            print(f"{i}\n")
        rows = len(m)
        colums = len(m[0])
        true_col = 0
        summ = 0
        negative = True
        for j in range(colums):
            for i in range(rows):
                if m[i][j] >= 0:
                    negative = False
                    break
                if negative:
                    true_col = j
        if true_col >= 0:
            for j in range(colums):
                for i in range(rows):
                    summ += m[i][j]
            return summ/rows
        else:
            print("Нет подхощях столбцов!")
    else:
        print("Неподходящий тип данных!")


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
