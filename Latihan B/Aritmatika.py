# Nama File   = Aritmatika.py
# Deskripsi   = membuat fungsi deret aritmatika dengan ekspresi rekursif 
# Nama        = akmal kafli anan
# Tanggal     = 30 September 2024

# Definisi Dan Spesifikasi 
# aritmatika: integer > 0 --> integer
#   {aritmatika(n)mengitung perjumlahan deret aritmatika dimulai dari 3 dan selanjutnya dengan masing masing deret dikali 3 menggunakan ekspresi rekursif}

# Realisasi
#   {F(1) = 3
#    f(2) = 3 + 6
#    f(n-1) = f(n) + n*3}
def aritmatika(n):
    if n == 1:
        return 3
    else:
        return aritmatika(n - 1) + (n * 3)

# Aplikasi
print(aritmatika(3))
print(aritmatika(4))
print(aritmatika(5))