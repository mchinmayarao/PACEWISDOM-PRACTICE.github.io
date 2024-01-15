def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    smaller = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

array = [3,1,6,9,5,7]
print(quick_sort(array))