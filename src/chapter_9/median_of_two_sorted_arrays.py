import math


def median_of_two_sorted_arrays(x, y):
    return median_of_two_sorted_arrays_internal(
        x, 0, len(x) - 1, y, 0, len(y) - 1)


def median_of_two_sorted_arrays_internal(x, px, rx, y, py, ry):
    if rx - px == 0 and ry - py == 0:
        return min(x[px], y[py])
    elif px > rx:
        return y[py]
    elif py > ry:
        return x[px]

    median_index_of_x = (px + rx) // 2
    median_index_of_y = (py + ry) // 2

    if x[median_index_of_x] < y[median_index_of_y]:
        return median_of_two_sorted_arrays_internal(
            x, median_index_of_x + 1, rx, y, py, median_index_of_y - 1)
    elif x[median_index_of_x] > y[median_index_of_y]:
        return median_of_two_sorted_arrays_internal(
            x, px, median_index_of_x - 1, y, median_index_of_y + 1, ry)
    else:
        return x[median_index_of_x]