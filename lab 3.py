def check_input(message):
    inp = -1
    try:
        inp = int(input(message))
    except ValueError:
        print("Ошибка ввода! Пожалуйста, повторите!")
    return inp


def task1():
    with open('F1.txt', 'w') as f:
        while True:
            line = input("Пожалуйста, введите строку (пустая строка - конец): ")
            if not line:
                break
            else:
                f.write(line + "\n")
    with open("F1.txt", "r") as rf, open("F2.txt", "w") as wf:
        while True:
            line = rf.readline()
            if not line:
                break
            words = line.split()
            d = {}
            for word in words:
                if word not in d:
                    d[word] = words.count(word)
            for k, v in d.items():
                if int(v) > 1:
                    wf.write(line)
    with open("F2.txt", 'r') as f:
        print(*f)


def task2():
    with open("число - число.txt", "r") as num_num:
        count = 1
        while True:
            line = num_num.readline()
            if not line:
                break
            elements = line.split(" ")
            if count == 1:
                elements[0] = "Один"
                count += 1
            elif count == 2:
                elements[0] = "Два"
                count += 1
            elif count == 3:
                elements[0] = "Три"
                count += 1
            elif count == 4:
                elements[0] = "Четыре"
                count += 1
            line = ' '.join(elements)
            print(line)
            with open("new_file.txt", "a") as new_file:
                new_file.write(line)


def task3():
    with open("предметы.txt", "r", encoding='utf-8') as subjects:
        amount_of_hours = {}
        summ = 0
        while True:
            line = subjects.readline()
            if not line:
                break
            print(line)
            index_for_start = line.find(":") + 2
            subject = line[0:index_for_start + 2]
            while index_for_start < len(line):
                summ += int(line[index_for_start:(line.find('('))])
                index_for_start = line.find("(") + 4
                if index_for_start > len(line):
                    break
                else:
                    line = line[index_for_start:len(line)]
                    index_for_start = 0
            amount_of_hours[subject] = summ
            summ = 0
    print(amount_of_hours)


def menu():
    choice = -1
    while choice != 0:
        print("\nВыберите:\n1.Task 1\n2.Task 2\n3.Task3")
        while choice < 0 or choice > 4:
            choice = check_input("\nВаш выбор - ")
        if choice == 1:
            task1()
            choice = -1
        elif choice == 2:
            task2()
            choice = -1
        elif choice == 3:
            task3()
            choice = -1


menu()
