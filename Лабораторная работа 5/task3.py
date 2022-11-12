from random import randint


def get_unique_list_numbers() -> list[int]:
    maxim = 10
    minim = -10
    count = 15  # TODO написать функцию для получения списка уникальных целых чисел
    list_numbers = [randint(minim, maxim) for i in range(count)]
    while len(list_numbers) != len(set(list_numbers)):
        list_numbers = [randint(minim, maxim) for i in range(count)]
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
