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
jumlah_input = 0
barang_belanjaan = []
jumlah_belanjaan = []
harga_belanjaan = []
item_khusus = "Diskon item khusus"
total_diskon_belanjaan = 0
diskon_belanjaan = []
a = 0
b = 0
while True:
    pembelian_barang = str(input( ))
    if pembelian_barang == kodeBarang_1:
        jumlah_input += 1
        jmlh_beli_barang = int(input( ))
        hargaBarang_1 *= jmlh_beli_barang
        barang_belanjaan.append(namaBarang_1)
        jumlah_belanjaan.append(jmlh_beli_barang)
        harga_belanjaan.append(hargaBarang_1)
        if jmlh_beli_barang > 10 : 
            diskon_khusus = diskonBarang_1 * hargaBarang_1
            diskon_khusus /= 100
            total_diskon_belanjaan += 1
            diskon_belanjaan.append(diskon_khusus)
        else:
            pass
        input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(y/n)"))
        if str.lower(input_ulang) == "y":
            pass
        elif str.lower(input_ulang) == "n":
            break
        if input_ulang == "n":
            break
    elif pembelian_barang == kodeBarang_2:
        jumlah_input += 1
        jmlh_beli_barang = int(input( ))
        hargaBarang_2 *= jmlh_beli_barang
        barang_belanjaan.append(namaBarang_2)
        jumlah_belanjaan.append(jmlh_beli_barang)
        harga_belanjaan.append(hargaBarang_2)
        if jmlh_beli_barang > 10 : 
            diskon_khusus = diskonBarang_2 * hargaBarang_2
            diskon_khusus /= 100
            total_diskon_belanjaan += 1
            diskon_belanjaan.append(diskon_khusus)
        else:
            pass
        input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(y/n)"))
        if str.lower(input_ulang) == "y":
            pass
        elif str.lower(input_ulang) == "n":
            break
        if input_ulang == "n":
            break
    elif pembelian_barang == kodeBarang_3:
        jumlah_input += 1
        jmlh_beli_barang = int(input( ))
        hargaBarang_3 *= jmlh_beli_barang
        barang_belanjaan.append(namaBarang_3)
        jumlah_belanjaan.append(jmlh_beli_barang)
        harga_belanjaan.append(hargaBarang_3)
        if jmlh_beli_barang > 10 : 
            diskon_khusus = diskonBarang_3 * hargaBarang_3
            diskon_khusus /= 100
            total_diskon_belanjaan += 1
            diskon_belanjaan.append(diskon_khusus)
        else:
            pass
        input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(y/n)"))
        if str.lower(input_ulang) == "y":
            pass
        elif str.lower(input_ulang) == "n":
            break
        if input_ulang == "n":
            break
        if input_ulang == "n":
            break
    else:
        print("Mohon maaf, barang tidak ditemukan")
print("\n=======================================")
print("Nama Brg | Jml | Total Harga |")
jumlah_print = 0
jumlah_print2 = 0
total_harga = sum(harga_belanjaan)
if total_harga > 1000000:
    while jumlah_input > jumlah_print:
        jumlah_print += 1
        print(barang_belanjaan[a], "|", jumlah_belanjaan[a], "|", harga_belanjaan[a], "|")
        a += 1
    print("=======================================")
    potongan_harga = total_harga * 5
    potongan_harga /= 100
    total_akhir = total_harga - potongan_harga
    print("Total Pembelian       | ", total_harga, " |")
    print("Diskon                | -",potongan_harga, " |")
    print("=======================================")
    print("Total Akhir           | ", total_akhir, " |")
elif total_harga < 1000000:
    if total_diskon_belanjaan > 0:
        while jumlah_input > jumlah_print:
            jumlah_print += 1
            print(barang_belanjaan[a], "|", jumlah_belanjaan[a], "|", harga_belanjaan[a], "|")
            while total_diskon_belanjaan > jumlah_print2 and jumlah_belanjaan[a] > 10:
                jumlah_print2 += 1
                print(item_khusus, "|", total_diskon_belanjaan, "| ", end= '-')
                print(diskon_belanjaan[b], "|")
                b += 1
            a += 1
    else:
        while jumlah_input > jumlah_print:
            jumlah_print += 1
            print(barang_belanjaan[a], "|", jumlah_belanjaan[a], "|", harga_belanjaan[a], "|")
            a += 1
    diskonAkhir = sum(diskon_belanjaan)
    totalAkhir = total_harga - diskonAkhir
    print("=======================================")
    print("Total Pembelian       | ", totalAkhir, " |")




