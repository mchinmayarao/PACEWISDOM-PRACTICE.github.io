def twoD_metrix_search(array,target):
    n = len(array)
    m = len(array[0]) if array else 0 

    i = 0
    j = m-1

    while( i<n and j>=0):
        if target == array[i][j]:
            return str(target) + " found at (" + str(i) + "," + str(j) +")"
        elif target > array[i][j]:
            i+=1
        elif target < array[i][j]:
            j-=1

array = [[10,20,30],[11,21,31],[12,22,32]]
target = 21

print(twoD_metrix_search(array,target))