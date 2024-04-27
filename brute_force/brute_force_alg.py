def count_rectangles_brute(data_points, data_rectangles):
    result = []
    for point in data_points:
        count = 0
        for rect in data_rectangles:
            x1, y1, x2, y2 = rect
            if x1 <= point[0] < x2 and y1 <= point[1] < y2:
                count += 1
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
#     # Вызов функции для подсчета принадлежности точек к прямоугольникам
#     result = count_rectangles_brute(points, rectangles)
#
#     # Вывод результатов
#     print(" ".join(map(str, result)))
