"""a = [2,4,5,6,7,9]
print(a)
b = [22,33,44,55,]
def mergesort(a,b):
    lena = len(a)
    lenb = len(b)
    sorted = []
    i=j=0
    while i< lena and j<lenb:
        if a[i] <= b[j]:
            sorted.append(a[i])
            i+=1
        else:
            sorted.append(b[j])
            j+=1
    while i<lena:
        sorted.append(a[i])
        i+=1
    while j<lenb:
        sorted.append(b[j])
        j+=1

    return sorted
print(mergesort(a,b))"""

elementa = [1,2,3,4,5,6,7,8,9]
elementb = [11,22,33,44,55,66,77,88,99]
def mergesort(elementa,elementb):
    lenea = len(elementa)
    leneb = len(elementb)
    sorted = []
    i = j = 0
    while i<lenea and i<leneb:
        if elementa[i] <= elementb[j]:
            sorted.append(elementa[i])
            i+=1
        else:
            sorted.append(elementb[j])
            j+=1
    while i<lenea :
        sorted.append(elementa[i])
        i+=1
    while j<leneb:
        sorted.append(elementb[j])

    return sorted
mergesort(elementa, elementb)

print(sorted)
















