k = 5


def select(numbers, i):
    assert i <= len(numbers)

    return select_internal(numbers, 0, len(numbers) - 1, i)


def select_internal(numbers, p, r, i):
    if p == r:
        return numbers[p]

    median = find_median_recursively(numbers, p, r)
    q = partition(numbers, p, r, median)
    k = q - p + 1

    if i == k:
        return numbers[q]
    elif i < k:
        return select_internal(numbers, p, q - 1, i)
    else:
        return select_internal(numbers, q + 1, r, i - k)


def partition(numbers, p, r, pivot):
    pivot_index = numbers.index(pivot, p)
    numbers[pivot_index], numbers[r] = numbers[r], numbers[pivot_index]

    i = p - 1

    for j in range(p, r):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i + 1], numbers[r] = numbers[r], numbers[i + 1]

    return i + 1


def find_median_recursively(numbers, p, r):
    medians = []

    for i in range(p, r + 1, k):
        if i + k - 1 <= r:
            insertion_sort(numbers, i, i + k - 1)

            medians.append(numbers[i + get_median_index(k)])
        else:
            insertion_sort(numbers, i, r)

            medians.append(numbers[i + get_median_index(r - i + 1)])

    if len(medians) == 1:
        return medians[0]
    else:
        return find_median_recursively(medians, 0, len(medians) - 1)


def get_median_index(length):
    if length % 2 == 1:
        return length // 2
    else:
        return length // 2 - 1


def insertion_sort(numbers, start, end):
    for i in range(start + 1, end + 1):
        j = i - 1
        key = numbers[i]

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key
