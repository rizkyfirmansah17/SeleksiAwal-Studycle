
arraybil = []
x = int(input("Masukan Jumlah Bilangan : "))

# Memasukan Bilangan Kedalam Array
for i in range(x):
    inputbil = float(input("Masukan Bilangan ke-{} : ".format(i+1)))
    arraybil.append(inputbil)

# Operasi Mengurutkan Nilai dari Nilai Terkecil
print("Daftar Bilangan : ", arraybil)
sort_terkecil = sorted(arraybil)

# Operasi Mengurutkan Nilai dari Nilai Terbesar
sort_terbesar = sorted(arraybil, reverse=True)

# Operasi Mencari Nilai Rata-Rata
mean = sum(arraybil)/x

# Operasi Mencari Nilai Tengah
mid = len(sort_terkecil) // 2
median = (sort_terkecil[mid] + sort_terkecil[~mid]) / 2

# Operasi Perkalian
perkalian = 1
for y in arraybil :
    perkalian *= y


print("\nSilahkan Pilih Nomor Operasi yang Akan Ditampilkan")
print("1 = Mengurutkan Bilangan dari Terkecil"
      "\n2 = Mengurutkan Bilangan dari Terbesar"
      "\n3 = Nilai Rata-Rata"
      "\n4 = Nilai Tengah"
      "\n5 = Hasil Perkalian Semua Bilangan"
      "\n0 = Keluar")

menu = ""
while menu != 0:
    menu = int(input("\nNomor Operasi yang Dipilih : "))
    if menu == 1:
        print("Mengurutkan Bilangan dari Terkecil : ", sort_terkecil)
    elif menu == 2:
        print("Mengurutkan Bilangan dari Terbesar : ", sort_terbesar)
    elif menu == 3:
        print("Nilai Rata-Rata : ", mean)
    elif menu == 4:
        print("Nilai Tengah : ", median)
    elif menu == 5:
        print("Nilai Hasil Perkalian Semua Bilangan : ", perkalian)
    elif menu == 0:
        print("Terimakasih & Sampai Jumpa")
    else:
        print("Nomor Tidak Terdaftar, Mohon Masukan Nomor Lain"
              "\n1 = Mengurutkan Bilangan dari Terkecil"
              "\n2 = Mengurutkan Bilangan dari Terbesar"
              "\n3 = Nilai Rata-Rata"
              "\n4 = Nilai Tengah"
              "\n5 = Hasil Perkalian Semua Bilangan"
              "\n0 = Keluar")