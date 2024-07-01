def majority_element(arr):
    if len(arr) == 0:
        return None
    me = arr[0]
    count = 1
    for i in range(1,len(arr)):
        if(arr[i]==me):
            count+=1
        elif count == 0:
            me = arr[i]
        else:
            count -=1

    

    if arr.count(me) > (len(arr)//2):
        return me
    else:
        return None

arr = [3, 3, 4, 2, 3, 3, 3]
print(majority_element(arr))
arr = [-1, -1, -1, -2, -1]
print(majority_element(arr))  
arr = [9, 9, 9, 10, 10, 10]
print(majority_element(arr)) 
