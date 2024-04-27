class Point:
    # Класс для представления точек на плоскости
    def __init__(self, x_coord: int, y_coord: int):
        # Инициализация координат точки
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __repr__(self):
        # Представление точки в виде строки
        return f"({self.x_coord}, {self.y_coord})"


class Rectangle:
    # Класс для представления прямоугольников на плоскости
    def __init__(self, first_point: Point, second_point: Point):
        # Инициализация координат углов прямоугольника
        self.first_point = first_point
        self.second_point = second_point

    def __repr__(self):
        # Представление прямоугольника в виде строки
        return f"[{self.first_point}, {self.second_point}]"


class TreeNode:
    # Узел персистентного дерева отрезков
    def __init__(self, val, left=None, right=None, left_index=None, right_index=None):
        # Инициализация узла
        self.val = val
        self.left = left
        self.right = right
        self.left_index = left_index
        self.right_index = right_index


class SegmentTreeEvent:
    # Событие для персистентного дерева отрезков
    ADD = 1
    REMOVE = -1

    def __init__(self, x_coord, begin_y, end_y, event_check):
        # Инициализация события
        self.x_coord = x_coord
        self.begin_y = begin_y
        self.end_y = end_y
        self.event_check = event_check


def binary_search(array, target):

    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return right


def compress_coordinates(data_rectangles: [Rectangle]):
    # Сжатие координат прямоугольников
    all_x = set()
    all_y = set()

    for rect in data_rectangles:
        all_x.update({rect.first_point.x_coord, rect.second_point.x_coord})
        all_y.update({rect.first_point.y_coord, rect.second_point.y_coord})

    compress_x = sorted(all_x)
    compress_y = sorted(all_y)

    return compress_x, compress_y


def add_node(node, begin, end, value):
    # Добавление узла к персистентному дереву отрезков
    if end <= node.left_index or node.right_index <= begin:
        return node

    if begin <= node.left_index and node.right_index <= end:
        return TreeNode(node.val + value, node.left, node.right, node.left_index, node.right_index)

    new_node = TreeNode(node.val, node.left, node.right, node.left_index, node.right_index)

    new_node.left = add_node(new_node.left, begin, end, value)
    new_node.right = add_node(new_node.right, begin, end, value)

    return new_node


def build_segment_tree(array, left_index, right_index):
    # Построение дерева отрезков
    if left_index + 1 == right_index:
        return TreeNode(array[left_index], None, None, left_index, right_index)

    middle = (left_index + right_index) // 2
    left = build_segment_tree(array, left_index, middle)
    right = build_segment_tree(array, middle, right_index)

    return TreeNode(left.val + right.val, left, right, left_index, right_index)


def build_persistent_segment_tree(data_rectangles, compress_x, compress_y):
    # Построение персистентного дерева отрезков
    if not data_rectangles:
        return None

    tree_events = []
    tree_roots = []

    for rectangle in data_rectangles:
        x1_idx = binary_search(compress_x, rectangle.first_point.x_coord)
        y1_idx = binary_search(compress_y, rectangle.first_point.y_coord)
        x2_idx = binary_search(compress_x, rectangle.second_point.x_coord)
        y2_idx = binary_search(compress_y, rectangle.second_point.y_coord)

        tree_events.extend([
            SegmentTreeEvent(x1_idx, y1_idx, y2_idx, SegmentTreeEvent.ADD),
            SegmentTreeEvent(x2_idx, y1_idx, y2_idx, SegmentTreeEvent.REMOVE)
        ])

    tree_events.sort(key=lambda element: element.x_coord)

    arr_root = [0] * len(compress_y)
    root = build_segment_tree(arr_root, 0, len(compress_y))

    x_end = tree_events[0].x_coord

    for event in tree_events:
        if x_end != event.x_coord:
            tree_roots.append(root)
            x_end = event.x_coord

        root = add_node(root, event.begin_y, event.end_y, event.event_check)

    tree_roots.append(root)

    return tree_roots


def sum_nodes_until_index(tree_node, value):
    # Суммирование значений узлов до заданного индекса
    if tree_node is not None:
        mid = (tree_node.left_index + tree_node.right_index) // 2

        if value < mid:
            return tree_node.val + sum_nodes_until_index(tree_node.left, value)
        else:
            return tree_node.val + sum_nodes_until_index(tree_node.right, value)

    return 0


def data_tree_prepare(data_points, data_rectangles):
    # Подготовка данных для персистентного дерева отрезков
    compressed = compress_coordinates(data_rectangles)
    comp_x, comp_y = compressed
    roots_tree = build_persistent_segment_tree(data_rectangles, comp_x, comp_y)

    return data_points, comp_x, comp_y, roots_tree


def persistent_segment_tree(data_points, compress_x, compress_y, root):
    # Вычисление результатов с использованием персистентного дерева отрезков
    result = [0] * len(data_points)

    if not root:
        return result

    for i, point in enumerate(data_points):
        position_x = binary_search(compress_x, point.x_coord)
        position_y = binary_search(compress_y, point.y_coord)

        if position_x >= 0 and position_y >= 0:
            result[i] = sum_nodes_until_index(root[position_x], position_y)
        else:
            result[i] = 0

    return result

# Source код для проверки правильности работы алгоритма
# if __name__ == "__main__":
#
#     num_rectangles = int(input())
#     rectangles = []
#
#     for _ in range(num_rectangles):
#         x1, y1, x2, y2 = map(int, input().split())
#         rectangles.append(Rectangle(Point(x1, y1), Point(x2, y2)))
#
#     num_points = int(input())
#     points = []
#
#     for _ in range(num_points):
#         x, y = map(int, input().split())
#         points.append(Point(x, y))
#
#     points, compressed_x, compressed_y, roots = data_tree_prepare(points, rectangles)
#
#     answer = persistent_segment_tree(points, compressed_x, compressed_y, roots)
#     print(" ".join(map(str, answer)))

