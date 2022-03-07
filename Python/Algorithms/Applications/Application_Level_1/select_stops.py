def select_stops(water_stops, capacity):
    # list of stops to visit
    stop_list = []

    # last stop visited
    prev_stop = 0

    for i in range(len(water_stops)):
        # if i cannot be reached, stop at i - 1
        if water_stops[i] - prev_stop > capacity:
            stop_list.append(water_stops[i - 1])
            prev_stop = water_stops[i - 1]

    # always stop on the last stop
    stop_list.append(water_stops[-1])

    return stop_list


# test
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))

# First Try

# def select_stops(water_stops, capacity):
#     # add index 0 as starting point
#     new_stops = [0] + water_stops
#     current = new_stops[0]
#     list_stops = []
#
#     for index1 in range(len(new_stops)):
#         # skip the stations until current
#         if new_stops[index1] != current:
#             continue
#         elif new_stops[index1] == new_stops[-1]:
#             break
#
#         max_distance = 0
#         destination = 0
#
#         for index2 in range(index1 + 1, len(new_stops)):
#             distance = new_stops[index2] - new_stops[index1]
#
#             if distance <= capacity:
#                 max_distance = max(max_distance, distance)
#                 destination = new_stops[index2]
#
#         current = destination
#         list_stops.append(current)
#
#     return list_stops
