def merge(left, right):
    result = []
    i, j =0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    mid = int(len(lst)/2)

    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    return merge(left, right)

lst = [9, -10, -4, -2, 0, 1 , 4, 2]
print(mergeSort(lst))