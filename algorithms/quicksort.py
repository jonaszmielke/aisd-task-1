def quicksort(array:list, start:int, end:int):
    """
    param start: start position of the subarray 
    param end: end position of the subarray
    """
    if start >= end:
        return

    pivot_index = partition(array, start, end)

    quicksort(array, start, pivot_index - 1)
    quicksort(array, pivot_index + 1, end)

def partition(array:list, start:int, end:int):
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Place the pivot in the correct position
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


if __name__ == "__main__":

    data = [5, 4, 1, 7, 0, 2, 3, 8]
    quicksort(data, 0, len(data) - 1)
    print(data)