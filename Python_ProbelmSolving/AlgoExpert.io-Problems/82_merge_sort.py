def merge(left, right):
    i,j = 0,0
    result = []

    while i<len(left) and j<len(right):
        if(left[i] < right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    result.extend(left[i:])
    result.extend(right[j:])

    return result 

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right) 

lst = [100, -1, 0, 200, 500, 69, 420]
print(merge_sort(lst))