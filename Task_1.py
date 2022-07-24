def linear_search(array):
    return (array.index(0) if 0 in array else False)


input_array = '11111111111100000000'
b = input_array.find('10') + 1
print(f"Функции Python: {b}")
array = list(input_array)
array = list(map(int, array))
print(f'Линейный поиск: {linear_search(array)}')
