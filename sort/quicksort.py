unsorted_list = [5, 8, 7, 3, 2, 9, 1, 2, 1]

def quick_sort(arr):
    # 배열의 길이가 1 이하일 경우, 이미 정렬된 배열로 반환
    if len(arr) <= 1:
        return arr
    
    # pivot 선택 (배열의 첫 번째 원소를 pivot으로 선택)
    pivot = arr[0]

    # pivot보다 작은 수와 큰 수로 나누기
    less = []
    greater = []

    for x in arr[1:]:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + [pivot] + quick_sort(greater)

sorted_list = quick_sort(unsorted_list)
print(sorted_list)