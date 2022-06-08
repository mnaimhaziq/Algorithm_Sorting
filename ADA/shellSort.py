def shell_sort(list):
    n = len(list) # Storing the length of the list into n
    gap = n // 2 #calculate the gap size
    while gap > 0: #sort array
        for i in range(gap, n): #insertion sort
            temp = list[i] #store list[i] into temp
            j = i
            while j >= gap and list[j - gap] > temp: 
                list[j] = list[j - gap]
                j -= gap

            list[j] = temp
        gap = gap // 2  # re-calculate the gap size


list = [16, 30, 95, 51, 84, 23, 62, 44] # unsorted list

print('Array before Sorting:')
print(list) # printing unsorted list
shell_sort(list) # call shell sort function a
print('Array after Sorting:')
print(list) # printing sorted list


