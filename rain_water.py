def rain_water(array):
    n = len(array)

    left_max = []
    right_max = []

    left_max.append(array[0]) #initializing left_max with first element of array
    right_max.append(array[-1]) #initializing right_max with last element of array

    for i in range(1, n):
        left_max.append(max(left_max[i - 1], array[i]))  #calculating the left max array

    for i in range(n - 2, -1, -1):
        right_max.append(max(right_max[-1], array[i])) #calculating the right max array

    right_max = right_max[::-1]  #reversing the right_max array for correction

    water = 0

    for i in range(1,n-1):
        water += max(0, min(left_max[i], right_max[i]) - array[i])
    
    return water
array = [2, 3, 1, 4, 5, 2, 1, 7, 2]

print(rain_water(array))
