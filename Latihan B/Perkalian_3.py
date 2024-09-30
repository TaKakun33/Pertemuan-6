# Nama File   = Perkalian_3.py
# Deskripsi   = membuat fungsi perkalian kali 3 dengan ekspresi rekursif 
# Nama        = akmal kafli anan
# Tanggal     = 30 September 2024

# Definisi Dan Spesifikasi 
# perkalian3: integer > 0 --> integer
#   {perkalian3(n)mengitung perkalian dari input n dengan 3 dengan menggunakan ekspresi rekursif}

# Realisasi
#   {F(1) = 3
#    f(n-1) = f(n) + 3}
def perkalian3(n):
    if n == 1:
       return  3
    else:
       return perkalian3(n-1) + 3
   
# Aplikasi
print(perkalian3(2))
print(perkalian3(5))
print(perkalian3(9))