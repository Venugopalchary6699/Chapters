def insertsort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor
elements = [33,2,4,11,5,32,5,3]
insertsort(elements)
print(elements)
def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor

elements = [11,9,29,7,2,14,15,28]
insertion_sort(elements)
print(elements)