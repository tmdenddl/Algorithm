def course_selection(course_list):
    # sort the course_list by earliest finishing time
    sorted_list = sorted(course_list, key=lambda x: x[1])

    # take the course that finishes the earliest of all
    my_selection = [sorted_list[0]]

    # choose a course that does not overlap with the ones already chosen and finishes the earliest
    for course in sorted_list:
        # if the course begins before the last one finishes, it overlaps
        if course[0] >= my_selection[-1][1]:
            my_selection.append(course)

    return my_selection


# Test
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
