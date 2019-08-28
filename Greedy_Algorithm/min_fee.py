def min_fee(pages_to_print):
    # total to be paid
    total = 0

    # sort by ascending order
    people = sorted(pages_to_print)

    # choose the person with the smallest value every time
    for i in range(len(people)):
        total += people[i] * (len(people) - i)

    return total


# Test
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
