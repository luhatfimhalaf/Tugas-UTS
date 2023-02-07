namaBarang_1 = str(input("Masukkan Nama Barang1: "))
kodeBarang_1 = str(input("Masukkan Kode Barang1: "))
hargaBarang_1 = float(input("Masukkan Harga Barang1: "))
jumlahBarang_1 = int(input("Masukkan Jumlah Barang1: "))
diskonBarang_1 = float(input("Masukkan Diskon Barang1: "))
namaBarang_2 = str(input("Masukkan Nama Barang2: "))
kodeBarang_2 = str(input("Masukkan Kode Barang2: "))
hargaBarang_2 = float(input("Masukkan Harga Barang2: "))
jumlahBarang_2 = int(input("Masukkan Jumlah Barang2: "))
diskonBarang_2 = float(input("Masukkan Diskon Barang2: "))
namaBarang_3 = str(input("Masukkan Nama Barang3: "))
kodeBarang_3 = str(input("Masukkan Kode Barang3: "))
hargaBarang_3 = float(input("Masukkan Harga Barang3: "))
jumlahBarang_3 = int(input("Masukkan Jumlah Barang3: "))
diskonBarang_3 = float(input("Masukkan Diskon Barang3: "))
results = []
while True:
    pembelian_barang = str(input( ))
    if pembelian_barang == kodeBarang_1:
        jmlh_beli_barang = int(input( ))
        total_harga = jmlh_beli_barang*(hargaBarang_1-hargaBarang_1*diskonBarang_1)
        barang1 = namaBarang_1 + " | " + str(jmlh_beli_barang) + " | " + str(total_harga) + " |"
        results.append(barang1)
        input_ulang = str(input( "Apakah anda ingin menambah bar ang lagi?(y/n)"))
        if input_ulang == "n":
            break
    elif pembelian_barang == kodeBarang_2:
        jmlh_beli_barang = int(input( ))
        total_harga = jmlh_beli_barang*(hargaBarang_2-hargaBarang_2*diskonBarang_2)
        barang2 = namaBarang_2 + " | " + str(jmlh_beli_barang) + " | " + str(total_harga) + " |"
        results.append(barang2)
        input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(y/n)"))
        if input_ulang == "n":
            break
    elif pembelian_barang == kodeBarang_3:
        jmlh_beli_barang = int(input( ))
        total_harga = jmlh_beli_barang*(hargaBarang_3-hargaBarang_3*diskonBarang_3)
        barang3 = namaBarang_3 + " | " + str(jmlh_beli_barang) + " | " + str(total_harga) + " |"
        results.append(barang3)
        input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(y/n)"))
        if input_ulang == "n":
            break
    else:
        print("Mohon maaf, barang tidak ditemukan")
print("\n=======================================")
print("Nama Brg | Jml | Total Harga |")
for i in results:
    print(i)
print("=======================================")
