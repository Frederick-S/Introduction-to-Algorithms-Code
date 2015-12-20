def selection_sort(numbers):
    length = len(numbers)

    for i in range(length):
        min = i

        for j in range(i + 1, length):
            if numbers[min] > numbers[j]:
                min = j

        if min != i:
            numbers[min], numbers[i] = numbers[i], numbers[min]
