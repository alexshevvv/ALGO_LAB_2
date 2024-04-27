import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2, 11)

# Данные для прямой brute_alg
brute_alg = [35.1994, 58.2205, 103.1282, 180.7307, 335.2329, 687.4985, 1319.0234, 2646.6270, 5364.7586, 10853.1710][:len(x)]

# Данные для прямой with_data_prep_map
with_data_prep_map = [189.4499, 217.7573, 231.990, 264.9492, 416.5793, 1223.1931, 8109.2278, 61318.2252, 463323.1721, 3512441.6772][:len(x)]

# Данные для прямой with_data_prep_segtree
with_data_prep_segtree = [188.92, 231.8372, 269.3668, 323.0298, 374.8011, 402.778, 475.7465, 567.6253, 712.7299, 817.166][:len(x)]

plt.plot(x, brute_alg, label='brute_alg', color='g')
plt.plot(x, with_data_prep_map, label='with_data_prep_map', color='b')
plt.plot(x, with_data_prep_segtree, label='with_data_prep_segtree', color='m')

plt.xlabel('Степени i, 2^i')
plt.ylabel('Время работы (миллисекунды)')
plt.title('Сравнение показателей времени работы алгоритмов с учётом подготовки данных')
plt.grid(True)


plt.yscale('log')
plt.legend()
plt.show()
