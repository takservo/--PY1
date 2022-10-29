def get_count_char(str_):
    str_ = str_.split()
    str_ = "".join(str_)
    str_ = str_.lower()  # TODO посчитать количество каждой буквы в строке в аргументе str_
    char_dict = {}
    default_count = 0
    for char in str_:
        if char.isalpha():
           char_dict[char] = char_dict.get(char, default_count) + 1
    return char_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


def get_percent_char(dic_):
    summa = 0
    percent_dict = {}
    for char in dic_:
        summa += dic_[char]
    for char in dic_:

        percent_dict[char] = percent_dict.get(char, dic_[char]/summa*100)
    return percent_dict


print(get_percent_char(get_count_char(main_str)))
