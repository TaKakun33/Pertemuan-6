# Nama File   = Pemangkatan.py
# Deskripsi   = membuat fungsi pengurangan dengan ekspresi rekursif 
# Nama        = akmal kafli anan
# Tanggal     = 30 September 2024

# Definisi Dan Spesifikasi 
# pemangkatan: integer > 0, integer > 0 --> real
#   {pemangkatan(x,y)mengitung pemangkatan dari kedua input yaitu dari x dipangkat dengan y dengan menggunakan ekspresi rekursif}

# Realisasi
def pemangkatan(x,y):
    if y == 1:
        return x
    else:
        return (pemangkatan(x,y-1)* x) 

# Aplikasi
print(pemangkatan(2,3))
print(pemangkatan(4,2))
print(pemangkatan(5,6))