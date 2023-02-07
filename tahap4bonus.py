#MEMBUAT PROGRAM KASIR SEDERHANA TANPA FUNCTION
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
jumlahInput = 0
barangBelanjaan = []
jumlahBelanjaan = []
hargaBelanjaan = []
ItemKhusus = "Diskon item khusus"
totalDiskonBelanjaan = 0
diskonIKbelanjaan = []
x = 0
y = 0
while True:
    pembelian_barang = input("")
    if pembelian_barang == kodeBarang_1:
        jumlahInput += 1
        jmlh_beli_barang = int(input(""))
        hargaBarang_1 *= jmlh_beli_barang
        barangBelanjaan.append(namaBarang_1)
        jumlahBelanjaan.append(jmlh_beli_barang)
        hargaBelanjaan.append(hargaBarang_1)
        if jmlh_beli_barang > 10:
            diskonItemKhusus = diskonBarang_1 * hargaBarang_1
            diskonItemKhusus /= 100
            totalDiskonBelanjaan += 1
            diskonIKbelanjaan.append(diskonItemKhusus)
        else:
            pass
        lanjutInput = input("Apakah anda ingin menambah barang lagi?(y/n)")
        if str.lower(lanjutInput) == "y":
            pass
        elif str.lower(lanjutInput) == "n":
            break
    elif pembelian_barang == kodeBarang_2:
        jumlahInput += 1
        jmlh_beli_barang = int(input(""))
        hargaBarang_2 *= jmlh_beli_barang
        barangBelanjaan.append(namaBarang_2)
        jumlahBelanjaan.append(jmlh_beli_barang)
        hargaBelanjaan.append(hargaBarang_2)
        if jmlh_beli_barang > 10:
            diskonItemKhusus = diskonBarang_2 * hargaBarang_2
            diskonItemKhusus /= 100
            totalDiskonBelanjaan += 1
            diskonIKbelanjaan.append(diskonItemKhusus)
        else:
            pass
        lanjutInput = input("Apakah anda ingin menambah barang lagi?(y/n)")
        if str.lower(lanjutInput) == "y":
            pass
        elif str.lower(lanjutInput) == "n":
            break
    elif pembelian_barang == kodeBarang_3:
        jumlahInput += 1
        jmlh_beli_barang = int(input(""))
        hargaBarang_3 *= jmlh_beli_barang
        barangBelanjaan.append(namaBarang_3)
        jumlahBelanjaan.append(jmlh_beli_barang)
        hargaBelanjaan.append(hargaBarang_3)
        if jmlh_beli_barang > 10:
            diskonItemKhusus = diskonBarang_3 * hargaBarang_3
            diskonItemKhusus /= 100
            totalDiskonBelanjaan += 1
            diskonIKbelanjaan.append(diskonItemKhusus)
        else:
            pass
        lanjutInput = input("Apakah anda ingin menambah barang lagi?(y/n)")
        if str.lower(lanjutInput) == "y":
            pass
        elif str.lower(lanjutInput) == "n":
            break
    else:
        print("Mohon maaf, barang tidak ditemukan")
print("\n=======================================")
print("Nama Brg | Jml | Total Harga |")
jumlahPrint = 0
jumlahPrint2 = 0
totalHarga = sum(hargaBelanjaan)
if totalHarga > 1000000:
    while jumlahInput > jumlahPrint:
        jumlahPrint += 1
        print(barangBelanjaan[x], "|", jumlahBelanjaan[x], "|", hargaBelanjaan[x], "|")
        x += 1
    print("=======================================")
    potonganHarga = totalHarga * 5
    potonganHarga /= 100
    totalAkhir = totalHarga - potonganHarga
    print("Total Pembelian       | ", totalHarga, " |")
    print("Diskon                | -",potonganHarga, " |")
    print("=======================================")
    print("Total Akhir           | ", totalAkhir, " |")
elif totalHarga < 1000000:
    if totalDiskonBelanjaan > 0:
        while jumlahInput > jumlahPrint:
            jumlahPrint += 1
            print(barangBelanjaan[x], "|", jumlahBelanjaan[x], "|", hargaBelanjaan[x], "|")
            while totalDiskonBelanjaan > jumlahPrint2 and jumlahBelanjaan[x] > 10:
                jumlahPrint2 += 1
                print(ItemKhusus, "|", totalDiskonBelanjaan, "| ", end= '-')
                print(diskonIKbelanjaan[y], "|")
                y += 1
            x += 1
    else:
        while jumlahInput > jumlahPrint:
            jumlahPrint += 1
            print(barangBelanjaan[x], "|", jumlahBelanjaan[x], "|", hargaBelanjaan[x], "|")
            x += 1
    diskonAkhir = sum(diskonIKbelanjaan)
    totalAkhir = totalHarga - diskonAkhir
    print("=======================================")
    print("Total Pembelian       | ", totalAkhir, " |")