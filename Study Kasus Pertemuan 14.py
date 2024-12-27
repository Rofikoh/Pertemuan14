import re

def validasi_input(nama, telepon, email):
    errors = []

    # Validasi nama lengkap (hanya huruf)
    if not nama.isalpha():
        errors.append("Nama lengkap harus hanya berisi huruf.")

    # Validasi nomor telepon (hanya angka)
    if not telepon.isdigit():
        errors.append("Nomor telepon harus hanya berisi angka.")

    # Validasi email (harus mengandung karakter @ dan .)
    if "@" not in email or "." not in email:
        errors.append("Email harus mengandung karakter '@' dan '.'.")

    # Jika tidak ada error, data valid
    if not errors:
        return "Data pendaftaran valid."
    else:
        return "\n".join(errors)

# Input dari pengguna
nama_lengkap = input("Masukkan nama lengkap: ")
nomor_telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

# Validasi input
hasil_validasi = validasi_input(nama_lengkap, nomor_telepon, email)

# Tampilkan hasil validasi
print(hasil_validasi)
