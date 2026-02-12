def selection_sort(arr):
    mid = len(arr) // 2
    left = selection_sort(arr[:mid])
    right = selection_sort(arr[mid:])
    sorted_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
numbers = [1,4,9,5,2]
print(selection_sort(numbers))