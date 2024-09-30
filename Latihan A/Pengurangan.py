# Nama File   = Pengurangan.py
# Deskripsi   = membuat fungsi pengurangan dengan ekspresi rekursif 
# Nama        = akmal kafli anan
# Tanggal     = 30 September 2024

# Definisi Dan Spesifikasi 
# pengurangan: integer > 0, integer > 0 --> integer
#   {pengurangan(x,y)mengitung pengurangan dari kedua input yaitu dari x dan y dengan menggunakan ekspresi rekursif}

# Realisasi
def pengurangan(x,y):
    if y == 0:
        return x
    else:
        return (pengurangan(x,y - 1)) -1
    
# Aplikasi
print(pengurangan(5,3))
print(pengurangan(2,2))
print(pengurangan(1,3))