txt = 'Hello World'

# Hitung jumlah karakternya
jumlah_karakter = len(txt)

# Ambil karakter terakhir
karakter_terakhir = txt[-1]

# Ambil karakter index ke-2 sampai index ke-4 (llo)
karakter_index_2_4 = txt[2:5]

# Hilangkan spasi pada text tersebut (HelloWorld)
hilangkan_spasi = txt.replace(" ", "")

# Ubah text menjadi huruf besar
huruf_besar = txt.upper()

# Ubah text menjadi huruf kecil
huruf_kecil = txt.lower()

# Ganti karakter H dengan karakter J
ganti_h_j = txt.replace("H", "J")

# Menampilkan hasil
print("Jumlah karakter:", jumlah_karakter)
print("Karakter terakhir:", karakter_terakhir)
print("Karakter index ke-2 sampai ke-4:", karakter_index_2_4)
print("Hilangkan spasi:", hilangkan_spasi)
print("Ubah ke huruf besar:", huruf_besar)
print("Ubah ke huruf kecil:", huruf_kecil)
print("Ganti H dengan J:", ganti_h_j)
