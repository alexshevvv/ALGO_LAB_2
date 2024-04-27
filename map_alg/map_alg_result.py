from time import perf_counter

from map_alg import *
from map_alg_generate import *

map_prepare_time = []
map_alg_time = []

num_rectangles = 2 ** 1
n = 10

for i in range(n):
    rectangles = generate_rectangles_map(num_rectangles)
    points = generate_points_map(num_rectangles, 100000)

    start_time = perf_counter()
    coordinate_map = build_map(rectangles, points)
    end_time = perf_counter()

    time_ms = (end_time - start_time) * 1000
    map_prepare_time.append(round(time_ms, 3))

    start_time = perf_counter()
    count_rectangles_map(*coordinate_map, points)
    end_time = perf_counter()

    time_ms = (end_time - start_time) * 1000
    map_alg_time.append(round(time_ms, 3))

print("Map preparation time:", map_prepare_time)
print()
print("Map algorithm time:", map_alg_time)
