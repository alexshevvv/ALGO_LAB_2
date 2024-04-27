import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2, 11)

# Данные для прямой brute_alg
brute_alg = [35.1994, 58.2205, 103.1282, 180.7307, 335.2329, 687.4985, 1319.0234, 2646.6270, 5364.7586, 10853.1710][:len(x)]

# Данные для прямой without_data_prep_map
without_data_prep_map = [175.2737, 203.3031, 215.6513, 234.9336, 281.4977, 298.8988, 364.4440, 400.9335, 437.0173, 524.4208][:len(x)]

# Данные для прямой without_data_prep_segtree
without_data_prep_segtree = [183.5451, 226.3481, 263.7129, 316.6414, 366.7100, 392.4712, 459.5159, 540.5957, 646.2446, 680.0213][:len(x)]


plt.plot(x, brute_alg, label='brute_alg', color='g')
plt.plot(x, without_data_prep_map, label='without_data_prep_map', color='b')
plt.plot(x, without_data_prep_segtree, label='without_data_prep_segtree', color='m')


plt.xlabel('Степени i, 2^i')
plt.ylabel('Время работы (миллисекунды)')
plt.title('Сравнение показателей времени работы алгоритмов без подготовки данных')
plt.grid(True)

plt.legend()
plt.show()


# Второй график - больший масштаб
plt.plot(x, brute_alg, label='brute_alg', color='g')
plt.plot(x, without_data_prep_map, label='without_data_prep_map', color='b')
plt.plot(x, without_data_prep_segtree, label='without_data_prep_segtree', color='m')

plt.xlabel('Степени i, 2^i')
plt.ylabel('Время работы (миллисекунды)')
plt.grid(True)

plt.yscale('log')
plt.legend()
plt.show()