def task1():
    some_int = 45 ** 34
    some_float = 3.14
    some_string = "String"
    some_tuple = (1, 2, 3)
    some_list = [i for i in range(0, 10)]
    some_set = set(some_tuple)
    some_dict = {
        "some_key1": "some_value1"
    }

    print(some_int, some_set, some_dict, some_list, some_tuple,
          some_string, some_float, sep='\n')
    some_input = input("some input = ")
    print("some_input = {}".format(some_input))


def task2():
        input_time = int(input("time : "))
        minutes = input_time // 60
        seconds = input_time % 60
        hours = minutes // 60 % 24
        minutes = input_time % 60
        print("hours: {}, minutes: {},seconds: {}"
              .format(hours, minutes, seconds))


def task3():
    n = input("Введите n : ")
    print("n + nn + nnn = {}".format(int(n) + int(n*2) + int(n*3)))


def task4():
    n = list(input("n : "))
    list_of_numbers = [int(i) for i in n]
    max_num = list_of_numbers[0]
    i = 0
    while(i < len(n)):
        if(list_of_numbers[i] > max_num):
            max_num = list_of_numbers[i]
        i += 1
    print(max_num)


def task5():
    revenuese = int(input("Выручка: "))
    costs = int(input("Издержки : "))
    if(revenuese > costs):
        print("Мы работаем с прибылью")
        print("Рентабельность =", revenuese / costs)
        number_of_workers = int(input("Количество работников : "))
        print("Прибыль на одного работника :", revenuese/number_of_workers)
    elif(revenuese < costs):
        print("Мы работаем с убытком")
    elif(revenuese == costs):
        print("Выручка равна издержкам, мы работаем в 0")


def task6():
    start = float(input("Введите результат спортсмена в первый день : "))
    number_to_stop_from = float(
        input("Введите предельное количество километров: "))
    counter = 1
    while(number_to_stop_from > start):
        print("{}-й день : {}".format(counter, start))
        start = start + start / 10
        counter += 1
    print("{}-й день : {}".format(counter, start))


if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()

