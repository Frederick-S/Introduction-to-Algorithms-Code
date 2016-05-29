import math
from .select import select


def k_closet(numbers, k):
    length = len(numbers)
    i = math.ceil(length / 2)

    median = select(numbers, i)
    b = [abs(numbers[j] - median) for j in range(length)]

    closet = []
    kth_smallest = select(b, k)

    for j in range(length):
        if abs(numbers[j] - median) < kth_smallest:
            closet.append(numbers[j])

    for j in range(length):
        if abs(numbers[j] - median) == kth_smallest:
            closet.append(numbers[j])

        if len(closet) >= k:
            break

    return closet
