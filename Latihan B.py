def perkalian3(n):
    if n == 1:
       return  3
    else:
       return perkalian3(n-1) + 3
   
print(perkalian3(2))

def jumlah(x):
    if x == 1:
        return 1
    else:
         return jumlah(x- 1) + x
    
print(jumlah(3))

def aritmatika(x):
    if x == 1:
        return 3
    else:
        return aritmatika(x-1) + x
    
print(aritmatika(3))

def geometri(x):
    if x == 1:
        return 1
    else:
        return geometri(x-1) * 3
    
print(geometri(3))

def deret_2(x):
    if x == 1:
        return 1
    else:
        return deret_2(x-1) + x**2
    
print(deret_2(4))