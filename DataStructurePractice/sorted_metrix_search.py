def sorted_metrix_search(target,arr,n,m):

    i,j = 0,m-1
    
    while i<m and j >=0:

        if arr[i][j] == target:
            return f"{target} found at [{i}][{j}]"
        elif arr[i][j] < target:
            i+=1
        else:
            j-=1

    return f"{target} not found"



target = 5
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
n = 3
m = 4

print(sorted_metrix_search(target,arr,n,m))