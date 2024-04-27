from time import perf_counter

from brute_force_alg import count_rectangles_brute
from brute_force_generate import *

brute_force_time = []

num_rectangles = 2 ** 1
n = 10

for i in range(n):
    rectangles = generate_rectangles_brute(num_rectangles)
    points = generate_points_brute(num_rectangles, 100000)

    start_time = perf_counter()
    count_rectangles_brute(points, rectangles)
    end_time = perf_counter()

    time_ms = (end_time - start_time) * 1000
    brute_force_time.append(round(time_ms, 3))

print("Brute force time:", brute_force_time)
