def partition(arr, left, right):
    divider = left
    pivot = right
    for i in range(left, right):
        if arr[i] < arr[pivot]:
            arr[i], arr[divider] = arr[divider], arr[i]
            divider += 1
    arr[pivot], arr[divider] = arr[divider], arr[pivot]
    return divider


def quicksort(arr, left, right):
    if left >= right:
        return

    p = partition(arr, left, right)
    quicksort(arr, left, p-1)
    quicksort(arr, p+1, right)
    print("arr: ", arr)

quicksort([5, 1, 0, 9, 3, 4, 6, 7], 0, 7)
