def counting_sort(arr):
    size = len(arr)
    output = [0] * size
    count = [0] * 100

    # count the number. for example how many number 1 in the list
    for i in range(0, size):
        count[arr[i]] += 1

    # sorting
    # reduce number of count
    for j in range(1, 100):
        count[j] += count[j-1]

    # sorting the number based on the count
    a = size-1
    while a >= 0:
        output[count[arr[a]]-1] = arr[a]
        count[arr[a]] -= 1
        a -= 1

    # put the number from the output slot to list back
    for k in range(0, size):
        arr[k] = output[k]


arr = [16, 30, 95, 51, 84, 23, 62, 44]

print("The unsorted array:")
print(arr)
counting_sort(arr)
print("The sorted array using Counting Sort are:")
print(arr)
