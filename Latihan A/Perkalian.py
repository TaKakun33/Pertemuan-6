# Nama File   = Perkalian.py
# Deskripsi   = membuat fungsi perkalian dengan ekspresi rekursif 
# Nama        = akmal kafli anan
# Tanggal     = 30 September 2024

# Definisi Dan Spesifikasi 
# perkalian: integer > 0, integer > 0 --> integer
#   {perkalian(x,y)mengitung perkalian dari kedua input yaitu dari x dan y dengan menggunakan ekspresi rekursif}

# Realisasi
def perkalian(x,y):
    if y == 0:
        return 0
    else:
        return (perkalian(x,y - 1)) + x
    
# Aplikasi
print(perkalian(5,3))
print(perkalian(0,9))