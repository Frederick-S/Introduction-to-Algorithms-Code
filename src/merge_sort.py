def merge_sort(numbers):
    merge_sort_internal(numbers, 0, len(numbers) - 1)

def merge_sort_internal(numbers, low, high):
    if low < high:
        middle = (low + high) / 2

        merge_sort_internal(numbers, low, middle)
        merge_sort_internal(numbers, middle + 1, high)
        merge(numbers, low, middle, high)

def merge(numbers, low, middle, high):
    i = 0
    j = 0
    n1 = middle - low
    n2 = high - middle - 1
    left_part = numbers[low:middle + 1]
    right_part = numbers[middle + 1:high + 1]


    for k in range(low, high + 1):
        if i <= n1 and j <= n2:
            if left_part[i] <= right_part[j]:
                numbers[k] = left_part[i]
                i += 1
            else:
                numbers[k] = right_part[j]
                j += 1
        elif i <= n1:
            numbers[k] = left_part[i]
            i += 1
        elif j <= n2:
            numbers[k] = right_part[j]
            j += 1
