unsorted_list = [5, 8, 7, 3, 2, 9, 1, 2, 1]

def selection_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

sorted_list = selection_sort(unsorted_list)
print(sorted_list)