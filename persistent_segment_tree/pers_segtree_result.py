from time import perf_counter

from persistent_segtree_alg import *
from pers_segtree_generate import *

tree_prepare_time = []
pers_segment_tree_alg_time = []

num_rectangles = 2 ** 1
n = 10

for i in range(n):
    rectangles = generate_rectangles(num_rectangles)
    points = generate_points(num_rectangles, 100000)

    start_time = perf_counter()
    args = data_tree_prepare(points, rectangles)
    end_time = perf_counter()

    time_ms = (end_time - start_time) * 1000
    tree_prepare_time.append((round(time_ms, 3)))

    start_time = perf_counter()
    persistent_segment_tree(*args)
    end_time = perf_counter()

    time_ms = (end_time - start_time) * 1000
    pers_segment_tree_alg_time.append((round(time_ms, 3)))

print("Tree preparation time:", tree_prepare_time)
print()
print("Persistent segment tree algorithm time:", pers_segment_tree_alg_time)
