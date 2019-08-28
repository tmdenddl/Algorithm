def find_same_number(some_list):
    # dictionary to save the elements visited
    elements_seen_so_far = {}

    for element in some_list:
        # if visited already, return the element
        if element in elements_seen_so_far:
            return element

        # else, save the element into the dictionary
        elements_seen_so_far[element] = True


# test
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
