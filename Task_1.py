def linear_search(array):
    return (array.index(0) if 0 in array else False)


def binary_search(array, element=0):
    i = 0
    while i < len(array) and array[i] != element:
        i += 1
    if i < len(array):
        return i
    else:
        return False


input_array = '111111111111111111111111100000000'
array = list(input_array)
array = list(map(int, array))
print(array)
print(f'Линейный поиск (O(n)): {linear_search(array)}')
print(f"Бинарный поиск (O(log(n))): {binary_search(array)}")
