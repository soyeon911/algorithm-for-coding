unsorted_list = [5, 8, 7, 3, 2, 9, 1, 2, 1]

def bubble_sort(arr):
    length = len(arr)
    # 배열 길이가 1 이하일 경우 정렬 불필요
    if length <= 1:
        return arr
    
    # 배열 길이만큼
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
bubble_sort(unsorted_list)

for i in range(len(unsorted_list)):
    print("%d " %unsorted_list[i], end = " ")