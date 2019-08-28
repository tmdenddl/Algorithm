def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height


# 테스트
print(trapping_rain([0, 3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# def trapping_rain(buildings):
#     """
#     가로 한 줄마다 비가 들어가는 칸을 세면 어떨까?
#
#     - 제일 높은 층에서 시작한다.
#     - 각 층 마다, 그 층수 만큼 높은 첫 빌딩과 마지막 빌딩 사이 공간 수 - 중간에 낀 빌딩 공간 수 를 계산 하면 그 층을 채우는 비 수가 나옴
#
#     """
#
#     # no rain can be trapped if less than 3 buildings exist
#     if len(buildings) < 3:
#         return 0
#
#     highest = max(buildings)
#     total_rain = 0
#
#     for current_floor in range(highest, -1, -1):
#         # positions of buildings, where given current_floor exists
#         indices = [i for i, building_height in enumerate(buildings) if building_height >= current_floor]
#         # no rain can be piled if only one building of that height exists
#         if len(indices) < 2:
#             continue
#         else:
#             _min = min(indices)
#             _max = max(indices)
#             number_of_buildings_between = len(indices) - 2  # minus _min and _max
#             total_rain += (_max - _min - 1) - number_of_buildings_between
#
#     return total_rain
#
#
# # 테스트
# print(trapping_rain([3, 0, 0, 2, 0, 4]))
# print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
