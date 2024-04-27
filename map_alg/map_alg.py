def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right


def compress_coordinates(data_rectangles, data_points):
    all_x = set()
    all_y = set()
    for rect in data_rectangles:
        all_x.add(rect[0])
        all_x.add(rect[2])
        all_y.add(rect[1])
        all_y.add(rect[3])
    for point in data_points:
        all_x.add(point[0])
        all_y.add(point[1])

    compr_x = sorted(list(all_x))
    compr_y = sorted(list(all_y))

    return compr_x, compr_y


def build_map(data_rectangles, data_points):
    compressed_x, compressed_y = compress_coordinates(data_rectangles, data_points)

    coord_map = [[0] * (len(compressed_y) - 1) for _ in range(len(compressed_x) - 1)]

    for rect in data_rectangles:
        x1_idx = binary_search(compressed_x, rect[0])
        x2_idx = binary_search(compressed_x, rect[2])
        y1_idx = binary_search(compressed_y, rect[1])
        y2_idx = binary_search(compressed_y, rect[3])

        for i in range(x1_idx, x2_idx):
            for j in range(y1_idx, y2_idx):
                coord_map[i][j] += 1

    return coord_map, compressed_x, compressed_y


def count_rectangles_map(coord_map, compr_x, compr_y, points):
    result = []

    for point in points:
        x, y = point
        x_idx = binary_search(compr_x, x)
        y_idx = binary_search(compr_y, y)

        if 0 <= x_idx < len(compr_x) - 1 and 0 <= y_idx < len(compr_y) - 1:
            count = coord_map[x_idx][y_idx]
        else:
            count = 0

        result.append(count)

    return result

# Source код для проверки правильности работы алгоритма
# if __name__ == "__main__":
#     # Чтение количества прямоугольников
#     num_rectangles = int(input())
#
#     # Считывание прямоугольников
#     rectangles = []
#     for _ in range(num_rectangles):
#         x1, y1, x2, y2 = map(int, input().split())
#         rectangles.append((x1, y1, x2, y2))
#
#     # Чтение количества точек
#     num_points = int(input())
#
#     # Считывание точек
#     points = []
#     for _ in range(num_points):
#         x, y = map(int, input().split())
#         points.append((x, y))
#
#     # Сжатие координат
#     compressed_x, compressed_y = compress_coordinates(rectangles, points)
#
#     # Построение карты
#     coord_map = build_map(rectangles, points)
#
#     # Вызов функции для подсчета принадлежности точек к прямоугольникам
#     result = count_rectangles_map(*coord_map, points)
#
#     # Вывод результатов
#     print(" ".join(map(str, result)))
