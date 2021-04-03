# [3,5,-4,8,11,1,-1,6] -> find pair of numbers which adds up to 10 

"""
Double For Loop Approach :
- Check for all the a[i], a[j] pair in the same array that sums up to targetSum.
- Return the list of lists of resultant pairs
- Time : O(N2) because double for loop approach
- Space : O(1)
"""
def two_number_sum_bruteForce(lst, targetSum):
    result = []
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if(lst[i] + lst[j] == 10):
                result.append([lst[i],lst[j]])



def two_number_sum_twoPointersApproach(lst, targetSum):
    if(len(lst) < 2):
        return []
    
    lst.sort()

    left_pointer = 0
    right_pointer = len(lst)-1
    

    while(left_pointer < right_pointer):
        temp = lst[left_pointer] + lst[right_pointer]
        print(temp)
        if(temp == targetSum):
            return [lst[left_pointer], lst[right_pointer]]
        elif(temp < targetSum):
            left_pointer += 1
        elif(temp > targetSum):
            right_pointer -= 1

    return []




lst = [3,5,-4,8,11,1,-1,6]
result = two_number_sum_twoPointersApproach(lst, 13)
print(result)