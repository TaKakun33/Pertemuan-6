# Nama File   = Geometri.py
# Deskripsi   = membuat fungsi deret geometri dengan ekspresi rekursif 
# Nama        = akmal kafli anan
# Tanggal     = 30 September 2024

# Definisi Dan Spesifikasi 
# geometri: integer > 0 --> integer
#   {geometri(n)mengitung perjumlahan deret geometri dimulai dari 3 dan selanjutnya dengan masing masing deret dikali 3 menggunakan ekspresi rekursif}

# Realisasi
#   {F(1) = 1
#    f(2) = 1 + 3
#    f(n-1) = f(n) + 3**n3}
def geometri(n):
    if n == 1:
        return 1
    else:
        return geometri(n - 1) + 3**(n - 1)

# Aplikasi
print(geometri(1))
print(geometri(2))
print(geometri(3))
print(geometri(4))