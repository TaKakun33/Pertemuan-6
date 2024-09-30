def perkalian3(n):
    if n == 1:
       return  3
    else:
       return perkalian3(n-1) + 3
   
print(perkalian3(2))

def deret(x):
    if x == 1:
        return 1
    else:
         return deret(x- 1) + x
    
print(deret(3))

def aritmatika(x):
    if x == 1:
        return 3
    else:
        return aritmatika(x-1) + x
    
print(aritmatika(3))

def geometri(x):
    if x == 1:
        return 3
    else:
        return geometri(x-1) * x
    
print(geometri(3))