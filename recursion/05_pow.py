# find the value of x raised to the power n
def pow(x,n):
    if (n == 0):
        return 1 
    a = pow(x,n//2)
    if n%2 == 0 :
        return a*a
    else:
        return a*a*x
    
print(pow(2.0000, 10))