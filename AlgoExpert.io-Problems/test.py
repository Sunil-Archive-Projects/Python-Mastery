def gcdVal (x, y):
        while(y):
                x,y = y,x%y
        if(x==1):
                return 1
        else:
                return 0


def solve (n, a):
#     Type your code here
        if(n<2):
                return 0
        sum = 0
        for i in range(n):
                for j in range(i+1,n):
                        if(gcdVal(a[i], a[j])):
                                print(sum)
                                sum = sum + (a[i] * a[j])
        return sum%1000000007


    
print(solve(5, [1,2,3,4,5]))