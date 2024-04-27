class Point:
    def __init__(self, x_coord: int, y_coord: int):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __repr__(self):
        return f"({self.x_coord}, {self.y_coord})"


class Rectangle:
    def __init__(self, first_point: Point, second_point: Point):
        self.first_point = first_point
        self.second_point = second_point

    def __repr__(self):
        return f"[{self.first_point}, {self.second_point}]"


def generate_points(n, m):
    basis_x = 3089
    basis_y = 6089

    points = []
    for i in range(m):
        x = (basis_x * i) ** 31 % (20 * n)
        y = (basis_y * i) ** 31 % (20 * n)
        points.append(Point(x, y))
    return points


def generate_rectangles(n):
    rectangles = []
    for i in range(n):
        x1 = 10 * i
        y1 = 10 * i
        x2 = 10 * (2 * n - i)
        y2 = 10 * (2 * n - i)
        rectangles.append(Rectangle(Point(x1, y1), Point(x2, y2)))
    return rectangles
