from variables import data
import functions
import math

sorted_list_asc = data.copy()
print(f'\nВибірка:\n{sorted_list_asc}\n')

sorted_list_asc.sort()

print("Ранжована вибірка:")
functions.print_list(sorted_list_asc)

# Величина вибірки
n = len(sorted_list_asc)
print(f'\n\nn = {n}')

# Розмах
x_max: float = sorted_list_asc[-1]
x_min: float = sorted_list_asc[0]
magnitude = x_max - x_min
print("\n\nРозмах:")
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
frequencies = functions.get_frequencies_list(intervals, sorted_list_asc)
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
median = functions.get_median(sorted_list_asc)
print(f'\nМедіана:\nMe = {median}')

# Мода
mode = functions.get_mode(midpoints, list(frequencies.values()), sorted_list_asc, intervals)
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











