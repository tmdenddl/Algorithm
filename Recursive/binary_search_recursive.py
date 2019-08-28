def binary_search(element, some_list, start_index=0, end_index=None):
    # calculate end_index if not given
    if end_index == None:
        end_index = len(some_list) - 1

    # base case: there is no longer any element in the list
    if start_index > end_index:
        return None

    midpoint = (start_index + end_index) // 2

    # base case: element found in the midpoint index
    if some_list[midpoint] == element:
        return midpoint
    elif some_list[midpoint] > element:
        return binary_search(element, some_list, start_index, midpoint - 1)  # search left
    else:
        return binary_search(element, some_list, midpoint + 1, end_index)  # search right


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
