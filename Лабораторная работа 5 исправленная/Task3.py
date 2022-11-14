from random import randint


def get_unique_list_numbers(maxim: int, minim: int, count: int) -> list[int]:
    list_numbers = []
    i = 0
    while i != count:
        number = randint(minim, maxim)
        if number not in list_numbers:
            list_numbers.append(number)
            i += 1
    return list_numbers


list_unique_numbers = get_unique_list_numbers(10, -10, 15)
print(list_unique_numbers, len(list_unique_numbers))
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
