# Nama File   = Deret_Sum1.py
# Deskripsi   = membuat fungsi deret pejumlahan dengan ekspresi rekursif 
# Nama        = akmal kafli anan
# Tanggal     = 30 September 2024

# Definisi Dan Spesifikasi 
# deret_Sum: integer > 0 --> integer
#   {deret_Sum(n)mengitung perjumlahan deret dimulai dari 1 dan selanjutnya dengan masing masing deret ditambah 1 menggunakan ekspresi rekursif}

# Realisasi
#   {F(1) = 1
#    f(2) = 1 + 2
#    f(n-1) = f(n) + n}
def deret_Sum(n):
    if n == 1:
        return 1
    else:
         return deret_Sum(n - 1) + n

# Aplikasi
print(deret_Sum(3))
print(deret_Sum(4))
print(deret_Sum(5))
