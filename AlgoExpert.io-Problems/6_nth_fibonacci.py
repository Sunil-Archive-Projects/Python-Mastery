# Fnd out the nth Fibnonacci number

n = 10

"""
Naive method. Expensive. Repetitive Calculations
Time : O(2^n)
Space : O(n) 
"""
def fib_recursive(n):
    if(n == 2):
        return 1
    elif(n == 1):
        return 0
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

print(fib_recursive(10))


"""
Memoization == Caching. 
Cache the results that are already calculated to make sure that it is not repeated
Pass and update the memoization dict each time
"""
def fib_memoization(n, memoize = {1:0, 2:1}):
    if(n in memoize):
        return memoize[n]
    else:
        memoize[n] = fib_memoization(n-1, memoize) + fib_memoization(n-2, memoize)
        return memoize[n]

print(fib_memoization(10))

def fib_iterative(n):
    lastTwo = [0, 1]
    counter = 3

    while(counter <= n):
        print(lastTwo)
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    
    """
    This method has a catch for 1 where the answer should be zero. In  all other cases return the lastTwo[1]
    """
    return lastTwo[1] if n > 1 else lastTwo[0]


print(fib_iterative(3))