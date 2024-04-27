import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2, 11)

# Данные для прямой data_prep_map
data_prep_map = [14.1762, 14.4542, 16.3387, 30.0156, 135.0816, 924.2943, 7744.7838, 60917.2917, 462886.1548, 3511917.2564][:len(x)]

# Данные для прямой data_prep_segtree
data_prep_segtree = [5.3749, 5.4891, 5.6539, 6.3884, 8.0911, 10.3068, 16.2306, 27.0296, 66.4853, 137.1447][:len(x)]

plt.plot(x, data_prep_map, label='data_prep_map', color='b')
plt.plot(x, data_prep_segtree, label='data_prep_segtree', color='m')

plt.xlabel('Степени i, 2^i')
plt.ylabel('Время работы (миллисекунды)')
plt.title('Сравнение показателей времени подготовки данных')
plt.grid(True)

plt.yscale('log')
plt.legend()
plt.show()
