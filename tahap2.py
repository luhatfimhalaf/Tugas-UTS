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
pembelian_barang = str(input( ))
if pembelian_barang == kodeBarang_1:
    jmlh_beli_barang = int(input( ))
    pesan_input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(y/n)"))
    if pesan_input_ulang == "y":
        for i in range():
            pembelian_barang = str(input( ))
            if pembelian_barang == kodeBarang_1:
                jmlh_beli_barang = int(input( ))
    print("\n=======================================\nNama Brg","|","Jml","|","Total Harga","|\n",namaBarang_1,"|",jmlh_beli_barang,"|",jmlh_beli_barang*(hargaBarang_1-hargaBarang_1*diskonBarang_1),"|")
    print("Nama Brg","|","Jml","|","Total Harga","|")
    print(namaBarang_1,"|",jmlh_beli_barang,"|",jmlh_beli_barang*(hargaBarang_1-hargaBarang_1*diskonBarang_1),"|")
elif pembelian_barang == kodeBarang_2:
    jmlh_beli_barang = int(input( ))
    print("=======================================")
    print("Nama Brg","|","Jml","|","Total Harga","|")
    print(namaBarang_2,"|",jmlh_beli_barang,"|",jmlh_beli_barang*(hargaBarang_2-hargaBarang_2*diskonBarang_2),"|")
elif pembelian_barang == kodeBarang_3:
    jmlh_beli_barang = int(input( ))
    print("=======================================")
    print("Nama Brg","|","Jml","|","Total Harga","|")
    print(namaBarang_3,"|",jmlh_beli_barang,"|",jmlh_beli_barang*(hargaBarang_3-hargaBarang_3*diskonBarang_3),"|")
else:
    print("Mohon maaf, barang tidak ditemukan")

