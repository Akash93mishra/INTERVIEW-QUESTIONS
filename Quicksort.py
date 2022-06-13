def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [33, 22, 88, 11, 44, 99, 55]
print(quick_sort(arr))
