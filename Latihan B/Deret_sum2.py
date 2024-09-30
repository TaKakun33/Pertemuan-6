# Nama File   = Deret_Sum3.py
# Deskripsi   = membuat fungsi deret pejumlahan dengan ekspresi rekursif 
# Nama        = akmal kafli anan
# Tanggal     = 30 September 2024

# Definisi Dan Spesifikasi 
# deret_Sum: integer > 0 --> integer
#   {deret_Sum(n)mengitung perjumlahan deret dimulai dari 1 dan selanjutnya dengan masing masing deret ditambah pangkat 2 dari n menggunakan ekspresi rekursif}

# Realisasi
#   {F(1) = 1
#    f(2) = 1 + 4
#    f(n-1) = f(n) + n**2}
def deret_2(n):
    if n == 1:
        return 1
    else:
        return deret_2(n-1) + n**2

# Apliasi
print(deret_2(2))
print(deret_2(3))
print(deret_2(4))