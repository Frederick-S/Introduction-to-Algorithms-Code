from ..chapter_2.insertion_sort import insertion_sort


def hybrid_quick_sort(numbers, k):
    quick_sort_internal(numbers, 0, len(numbers) - 1, k)
    insertion_sort(numbers)


def quick_sort_internal(numbers, p, r, k):
    if p < r and r - p + 1 > k:
        q = partition(numbers, p, r)

        quick_sort_internal(numbers, p, q - 1, k)
        quick_sort_internal(numbers, q + 1, r, k)


def partition(numbers, p, r):
    x = numbers[r]
    i = p - 1

    for j in range(p, r):
        if numbers[j] <= x:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i + 1], numbers[r] = numbers[r], numbers[i + 1]

    return i + 1
