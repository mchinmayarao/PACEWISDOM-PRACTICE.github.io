def maxWater(arr): 
    res = 0
    for i in range(1, len(arr)): 

        left = max(arr[:i+1])
       
        right = max(arr[i:]) 

        res += (min(left, right) - arr[i]) 
  
    return res 
  

def maxWater2(arr):
    length = len(arr)
    left_max = [arr[0]]
    for i in range(1,length):
        left_max.append(max(left_max[i-1],arr[i]))
    
    right_max = [0 for x in range(length)]
    
    right_max[length-1] = arr[-1]
    
    for i in range(length-2,-1,-1):
        right_max[i] = max(right_max[i+1],arr[i])
    
    res = 0
    for i in range(length):
        res += min(left_max[i],right_max[i]) - arr[i]
    return res
        

    

  
  
arr = [ 3, 0, 2, 0, 4]
print(maxWater  (arr))
