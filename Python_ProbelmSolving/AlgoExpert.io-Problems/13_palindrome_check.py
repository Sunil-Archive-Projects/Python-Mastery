str = "abcdcba"

def check_palindrome_listApproach(str):
    result = []
    for x in str[::-1]:
        result.append(x)

    return str == "".join(result)


def check_palindrome_leftRightPointers(str):
    left = 0
    right = len(str) - 1

    while(left < right):
        if(str[left] == str[right]):
            left+=1
            right-=1
        else:
            return False
    
    return True


def check_palindrome_recursive(str, i):
    j = len(str)-1-i
    if(i < j):
        return str[i] == str[j] and check_palindrome_recursive(str, i+1) 
    else:
        return True

print(check_palindrome_listApproach(str))
print(check_palindrome_leftRightPointers(str))
print(check_palindrome_recursive(str,0))
