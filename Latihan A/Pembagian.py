# Nama File   = Pembagian.py
# Deskripsi   = membuat fungsi pembagian dengan ekspresi rekursif 
# Nama        = akmal kafli anan
# Tanggal     = 30 September 2024

# Definisi Dan Spesifikasi 
# pembagian: integer > 0, integer > 0 --> real
#   {pembagian(x,y)mengitung pembagian dari kedua input yaitu dari x dan y dengan menggunakan ekspresi rekursif}

# Realisasi
def pembagian(x,y):
    if y == 1:
        return x
    else:
        return (pembagian(x,y-1)) / y
    
# Aplikasi
print(pembagian(4,2))
print(pembagian(6,2))
print(pembagian(1,2))