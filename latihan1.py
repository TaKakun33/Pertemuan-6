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

def perkalian(x,y):
    if y == 0:
        return 0
    else:
        return (perkalian(x,y - 1)) + x
    
print(perkalian(5,3))