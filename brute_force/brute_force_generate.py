def generate_points_brute(n, m):
    basis_x = 3089
    basis_y = 6089

    points = []
    for i in range(m):
        x = (basis_x * i) ** 31 % (20 * n)
        y = (basis_y * i) ** 31 % (20 * n)
        points.append((x, y))
    return points


def generate_rectangles_brute(n):
    rectangles = []
    for i in range(n):
        x1 = 10 * i
        y1 = 10 * i
        x2 = 10 * (2 * n - i)
        y2 = 10 * (2 * n - i)
        rectangles.append((x1, y1, x2, y2))
    return rectangles
