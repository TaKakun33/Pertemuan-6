def pengurangan(x,y):
    if y == 0:
        return x
    else:
        return (pengurangan(x,y - 1)) -1
    
print(pengurangan(25,3))

def perkalian(x,y):
    if y == 0:
        return 0
    else:
        return (perkalian(x,y - 1)) + x
    
print(perkalian(5,3))

def pembagian(x,y):
    if y == 1:
        return x
    else:
        return (pembagian(x,y-1)) / y
    
print(pembagian(4,2))

def pemangkatan(x,y):
    if y == 1:
        return x
    else:
        return (pemangkatan(x,y-1)* x) 
    
print(pemangkatan(2,3))