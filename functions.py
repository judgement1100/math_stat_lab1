import math


def print_list(list: list):
    for item in list:
        print(item, end=', ')

def get_intervals(x_start: float, interval_width: float, intervals_num: float):
    intervals: list[float] = []
    i = 0
    while i <= intervals_num:
        intervals.append(x_start)
        x_start += interval_width
        i += 1
    return intervals

def get_midpoints_list(intervals: list[float]):
    midpoints: list[float] = []
    for i in range(len(intervals) - 1):
        midpoints.append((intervals[i] + intervals[i + 1]) / 2)
    return midpoints

def get_frequencies_list(intervals: list[float], sorted_data: list[float]):
    frequencies: dict[int, float] = {}

    for j in range(1, len(intervals)):
        frequencies[j] = 0

    for i in range(len(sorted_data)):
        for j in range(len(intervals)):
            if sorted_data[i] < intervals[j]:
                frequencies[j] += 1
                break
    return frequencies

def get_omega_list(frequencies: list, n: int):
    """
    :param frequencies: list
    :param n: int
    :return:
    """
    omegas_list = []
    for i in range(len(frequencies)):
        omegas_list.append(float(frequencies[i]) / float(n))
    return omegas_list

def get_accumulated_drequency_list(frequencies: list):
    accumulated_frequencies = []
    accumulated_frequencies.append(frequencies[0])
    for i in range(1, len(frequencies)):
        accumulated_frequencies.append(accumulated_frequencies[i - 1] + frequencies[i])
    return accumulated_frequencies

def get_accumulated_omegas_list(omegas: list):
    accumulated_omegas = []
    accumulated_omegas.append(round(omegas[0], 2))
    for i in range(1, len(omegas)):
        accumulated_omegas.append(round(accumulated_omegas[i - 1] + omegas[i], 2))
    return accumulated_omegas

def get_total(nums: list):
    sum = 0
    for item in nums:
        sum += item
    return round(sum, 2)

def get_avg_x(midpoints: list, frequencies: list, n: int):
    if len(midpoints) != len(frequencies):
        raise Exception("Length of midpoint_list is not equal to frequencies_list (get_median fun).")
    avg_x = 0
    for i in range(len(midpoints)):
        avg_x += midpoints[i] * frequencies[i]
    avg_x /= n
    return round(avg_x, 2)

def get_median(data: list):
    return data[int(len(data) / 2)]

def get_mode(midpoints: list, frequencies: list, data: list, intervals: list):
    most_frequent_midpoint = midpoints[frequencies.index(max(frequencies))]
    x_start = x_end = 0
    for i in range(0, len(intervals) - 1):
        if most_frequent_midpoint > intervals[i] and most_frequent_midpoint < intervals[i + 1]:
            x_start = intervals[i]
            x_end = intervals[i + 1]
            break
    counter = 0
    sum: float = 0
    for elem in data:
        if elem > x_start and elem < x_end:
            counter += 1
            sum += elem
    return round(sum / float(counter), 2)

def get_dispersion(avg_x: float, n: int, frequencies: list, midpoints: list):
    sum: float = 0
    for i in range(len(frequencies)):
        sum += (frequencies[i] * (midpoints[i] - avg_x)**2) / n
    return round(sum, 2)

def get_avg_deviation(dispersion: float):
    return round(dispersion**0.5, 2)

def get_variation_coef(s, x_avg):
    return round(100 * s / x_avg, 2)

def get_asymmetry_coef(avg_x: float, n: int, frequencies: list, midpoints: list, s: float):
    sum: float = 0
    for i in range(len(frequencies)):
        sum += (frequencies[i] * (midpoints[i] - avg_x) ** 3) / (100 * s**3)
    return round(sum, 2)

def get_excess(avg_x: float, n: int, frequencies: list, midpoints: list, s: float):
    sum: float = 0
    for i in range(len(frequencies)):
        sum += (frequencies[i] * (midpoints[i] - avg_x) ** 4) / (100 * s**4)
    return round(sum - 3, 2)












