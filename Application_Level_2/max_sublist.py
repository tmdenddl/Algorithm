def sublist_max(profits, start, end):
    # base case
    if start == end:
        return profits[start]

    mid = (start + end) // 2

    left_max = sublist_max(profits, start, mid)
    mid_max = max_crossing_sum(profits, start, end)
    right_max = sublist_max(profits, mid + 1, end)

    return max(left_max, mid_max, right_max)


def max_crossing_sum(profit, start, end):
    mid = (start + end) // 2  # mid index

    '''
    calculate the max profit of the left part
    find max profit from mid index to 0 index
    '''
    left_sum = 0  # accumulated profit (left)
    left_max = profit[mid]  # max profit (left); reset to most right of left half

    for i in range(mid, start - 1, -1):
        left_sum += profit[i]
        left_max = max(left_max, left_sum)

    '''
    calculate the max profit of the right part
    find max profit from mid+1 index to end index
    '''
    right_sum = 0  # accumulated profit (right)
    right_max = profit[mid + 1]  # max profit (right); reset to most left of right half

    for i in range(mid + 1, end + 1):
        right_sum += profit[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


# test
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))
