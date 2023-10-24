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
                    wf.write(line + "\n")
    with open("F2.txt", 'r') as f:
        print(*f)


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

            choice = -1
        elif choice == 3:

            choice = -1


menu()
