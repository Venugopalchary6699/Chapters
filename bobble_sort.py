
list = [9,3,5,2,5,743,75,754,7845,653,56,73]


def bubblesort(list):
    size = len(list)
    for ii in range(size-1):
        for i in range(size - 1):
            if list[i] >= list[i + 1]:
                tmp = list[i + 1]
                list[i + 1] = list[i]
                list[i] = tmp
    return list
print(bubblesort(list))
print(elements)















