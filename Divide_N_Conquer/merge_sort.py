def merge(list1, list2):
    # index of list1 and list2
    i = 0
    j = 0

    # empty list
    merged_list = []

    # add elements in ascending order until one of the list is empty
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    # add rest of the elements to the list
    if i == len(list1):
        merged_list += list2[j:]
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list


# 합병 정렬
def merge_sort(my_list):
    # base case:
    if len(my_list) < 2:
        return my_list

    mid = len(my_list) // 2

    left_half = merge_sort(my_list[:mid])
    right_half = merge_sort(my_list[mid:])

    return merge(left_half, right_half)


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
