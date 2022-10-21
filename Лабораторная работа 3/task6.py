list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_value = list_numbers[0]
max_pos = 0
for pos, value in enumerate(list_numbers):
    if value > max_value:
        max_pos = pos
        max_value = value
list_numbers[max_pos], list_numbers[-1] = list_numbers[-1], list_numbers[max_pos]

print(list_numbers)
