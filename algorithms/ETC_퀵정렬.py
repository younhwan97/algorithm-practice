def quick_sort(arr, left, right):
    if left >= right: return

    pi = partition(arr, left, right)
    quick_sort(arr, left, pi - 1)
    quick_sort(arr, pi + 1, right)

def partition(arr, left, right):
    i, j = left, right
    pivot = arr[left]

    while i < j:
        while pivot < arr[j]:
            j -= 1
        while i < j and pivot >= arr[i]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[left] = arr[i]
    arr[i] = pivot
    return i

arr = [3, 7, 8, 1, 5, 9, 6, 10, 2, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)