def task1():
    list_of_diff_types = [
        [1], (1, 2), {"name": "Maksym"},
        1, 2.0, task4
    ]
    for i in list_of_diff_types:
        print(type(i))


"""2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""


def task2():
    some_words: list = input().split()
    length_words = len(some_words)
    for i in range(0, length_words, 2):
        if i < length_words - 1:
            some_words[i], some_words[i + 1] = some_words[i + 1], some_words[i]
    print(some_words)


"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict"""


def task3():
    print()


"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""


def task4():
    some_words: list = input().split()
    counter: int = 1
    for i in some_words:
        if len(i) <= 10:
            print(counter, ': ', i)
        else:
            print(counter, ': ', i[ : 11])
        counter += 1


"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них."""


def task5():
    n = 0
    list_of_n = [7, 5, 4, 3, 2, 1]
    while n != -1:
        n = int(input("Input: "))
        list_of_n.append(n)
        list_of_n.reverse()
        list_of_n.sort()
        list_of_n.reverse()
        print(list_of_n)


if __name__ == '__main__':
    task2()
