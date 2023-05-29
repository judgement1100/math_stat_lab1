import random

import variables
import variables
import functions
import math

# Було згенеровано випадкові числа і записано в файл variables,
# тому заново щораразу генерувати цей масив не треба
# rnd_nums_list = [round(random.random(), 4) for i in range(100)]
# print(rnd_nums_list)

# Згенеровані випадкові числа N(0,1)
rnd_nums_list = variables.rnd_nums.copy()
print(f'Згенеровані випадкові числа N(0,1):\n{rnd_nums_list}')

# Множення на мій номер в списку (6)
data = [round(item * 6, 3) for item in rnd_nums_list]
print(f'\nВибірка:\n{data}')

# Ранжування вибірки
data.sort()
print(f'\nРанжована вибірка:\n{data}')
n = len(data)
print(f'\nn = {n}')

# Розмах вибірки
x_max: float = data[-1]
x_min: float = data[0]
magnitude = x_max - x_min
print("\nРозмах:")
print(magnitude)

# Кількість інтервалів
print("\nКількість інтервалів:")
m: float = 1 + 3.322 * math.log(100, 10)
print(f'm = {m} = {round(m)}')

# Шириниа інтервалу
k: float = (x_max - x_min) / (m)
print(f"\nШирина інтервалу:\n{k} = {round(k)}")

# x початкове
k = float(round(k)) # rounding k
x_start = x_min - k / 2
print(f'\nx_поч = {x_start}')

# x_start = float(round(x_start)) # rounding x_start
m = round(m) # rounding m

# Розбиття на інтервали
intervals = functions.get_intervals(x_start, k, m)
print(f'\nІнтервали: {intervals}')

# Середини інтервалів
midpoints = functions.get_midpoints_list(intervals)
print(f'\nСередини інтервалів: {midpoints}')

# Частота
frequencies = functions.get_frequencies_list(intervals, data)
print(f'\nЧастоти: {frequencies.values()}')
freqs_total = functions.get_total(list(frequencies.values()))
print(f'sum = {freqs_total}')

# Частість
omegas = functions.get_omega_list(list(frequencies.values()), n)
print(f'\nЧастість: {omegas}')
omegas_total = functions.get_total(omegas)
print(f'sum = {omegas_total}')

# Накопичена частота
accumulated_frequencies = functions.get_accumulated_drequency_list(list(frequencies.values()))
print(f'\nНакопичена частота: {accumulated_frequencies}')

# Накопичена частість
accumulated_omegas = functions.get_accumulated_omegas_list(omegas)
print(f'\nНакопичена частість: {accumulated_omegas}')

# Середнє значення вибірки
avg_x = functions.get_avg_x(midpoints, list(frequencies.values()), n)
print(f'Середнє арифметичне: {avg_x}')

# Медіана
median = functions.get_median(data)
print(f'\nМедіана:\nMe = {median}')

# Мода
mode = functions.get_mode(midpoints, list(frequencies.values()), data, intervals)
print(f'\nМода:\nMo = {mode}')

# Дисперсія
dispersion = functions.get_dispersion(avg_x, n, list(frequencies.values()), midpoints)
print(f'\nДисперсія:\nD = {dispersion}')

# Середньоквадратичне відхилення
s = functions.get_avg_deviation(dispersion)
print(f'\nСередньоквадратичне відхилення:\ns = {s}')

# Коефіцієнт варіації
variation_coef = functions.get_variation_coef(s, avg_x)
print(f'\nКоефіцієнт варіації:\nnu = {variation_coef}')

# Коефіцієнт асиметрії
asymmetry_coef = functions.get_asymmetry_coef(avg_x, n, list(frequencies.values()), midpoints, s)
print(f'\nКоефіцієнт асиметрії:\nA = {asymmetry_coef}')

# Ексцес
excess = functions.get_excess(avg_x, n, list(frequencies.values()), midpoints, s)
print(f'\nЕксцес:\nE = {excess}')





















