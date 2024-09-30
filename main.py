def Factorial(x):
    if  x == 1:
        return 1
    else:
        return x * (Factorial(x-1))
        
print(Factorial(2))

def fibonaci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return( fibonaci(x - 1)) + (fibonaci(x - 2))
        
print(fibonaci(6))