from sys import maxint


def find_maximum_subarray_brute_force(numbers, low, high):
    start = -1
    end = -1
    max_sum = -maxint - 1

    for i in range(low, high + 1):
        current_sum = 0

        for j in range(i, high + 1):
            current_sum += numbers[j]

            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j

    return (start, end, max_sum)
