def bubble_sort(arr):
    tmp = 0
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                tmp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = tmp
        print(arr)

arr = [10, 2, 3, 1, 5, 6, 8]
bubble_sort(arr)