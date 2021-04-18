lst = [-10, -2, 0, 1, 4, 10, 999, 7689]
search_key = 999

def binary_search_recursivePythonicSearch(lst, search_key):
    mid = len(lst) // 2
    low = 0 
    high = len(lst)-1

    while(low < high):
        if(lst[mid] == search_key):
            return True
        elif(lst[mid] > search_key):
            return binary_search_recursivePythonicSearch(lst[0:mid], search_key)
        elif(lst[mid] < search_key):
            return binary_search_recursivePythonicSearch(lst[mid:], search_key)

    return False

def binary_search_recursive(lst, searchKey, left, right):
    if(left>right):
        return -1
    
    middle = (left + right) //2
    potentialMatch = lst[middle]

    if(potentialMatch == searchKey):
        return middle
    elif(potentialMatch > searchKey):
        return binary_search_recursive(lst, searchKey, left, middle-1)
    elif(potentialMatch < searchKey):
        return binary_search_recursive(lst, searchKey, middle+1, right)





def binary_search_iterative(lst, searchKey, left, right):
    while(left < right):
        mid = (left + right) // 2
        if(lst[mid] == searchKey):
            return mid
        elif(mid > searchKey):
            right = mid -1
        elif(mid < searchKey):
            left = mid + 1

    return -1




result = binary_search_recursivePythonicSearch(lst, search_key)
print(result)


result = binary_search_recursive(lst, search_key, 0, len(lst)-1)
print(result)

result = binary_search_iterative(lst, search_key, 0, len(lst)-1)
print(result)