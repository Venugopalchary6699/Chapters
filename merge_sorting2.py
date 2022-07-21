
"""
                                    mid2 = len(arr)
                                    middle = arr[:mid2]
                                    print(middle)
"""

def merge_sort(arr):
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return define(left,right)
def define(a,b):
    print(a,b)
arr = [2,4,2,4,2,4,2,5,2,5,2]
print(merge_sort(arr))


