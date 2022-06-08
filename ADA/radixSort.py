def counting_sort(list, expo):
    #make a slot to put the number
    size = len(list)
    output = [0]*size
    count = [0]*10

    for i in range(0, size):
        index = list[i] // expo
        count[index % 10] += 1
    for j in range(1, 10):
        count[j] += count[j-1]

    k = size-1
    while k >= 0:
        index = list[k] // expo
        output[count[index % 10]-1] = list[k]
        count[index % 10] -= 1
        k -= 1
    for a in range(0, size):
        list[a] = output[a]


def radix_sort(list):
    m = max(list)
    expo = 1
    while m/expo >= 1:
        counting_sort(list, expo)
        expo *= 10


list = [16, 30, 95, 51, 84, 23, 62, 44]
print("Before sorting:")
print(list)
radix_sort(list)
print("After sorting:")
print(list)
