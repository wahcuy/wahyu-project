# PROJECT UAS PRODAS

from tabulate import tabulate

nama = []
cari_pesanan = []

# List Daftar Menu
menuMakanan = [
    ["1", "Steak Ayam", "Rp. 25.000"],
    ["2", "Steak Sirlon Sapi", "Rp. 45.000"],
    ["3", "Steak Kambing", "Rp. 45.000"],
    ["4", "Nasi Gurih", "Rp. 15.000"],
    ["5", "Nasi Goreng", "Rp. 25.000"],
    ["6", "Mie Ayam", "Rp. 15.000"],
    ["7", "Dimsum Ayam", "Rp. 15.000"],
    ["8", "Dimsum Sapi", "Rp. 20.000"],
    ["9", "Dimsum Jamur", "Rp. 15.000"],
    ["10", "Keripik Ubi", "Rp. 5.000"],
]
hargaMakanan = [25000, 45000, 45000, 15000,
                25000, 15000, 15000, 20000, 15000, 5000]

menuMinuman = [
    ["1", "Jus Apel", "Rp. 15.000"],
    ["2", "Jus Jeruk", "Rp. 15.000"],
    ["3", "Jus Alpukat", "Rp. 15.000"],
    ["4", "Jus Mangga", "Rp. 15.000"],
    ["5", "Cappucino", "Rp. 15.000"],
    ["6", "Air Mineral", "Rp. 10.000"],
    ["7", "Kopi Tubruk", "Rp. 10.000"]
]
hargaMinuman = [15000, 15000, 15000, 15000, 15000, 10000, 10000]

menuTambahan = [
    ["A", "Nasi Uduk", "Rp. 5.000"],
    ["B", "Nasi Putih", "Rp. 5.000"],
    ["C", "Kuah Soto", "Rp. 5.000"],
]
hargaTambahan = [5000, 5000, 5000, 0]

print("================================================")
print("Daftar Menu Cafe WAHYU")
print("================================================")
print("\n Menu Makanan")
print(tabulate(menuMakanan, tablefmt="grid", headers=[
      "No.", "Menu Makanan", "Tarif"], numalign="center", stralign="center"))
print("\n Menu Minuman")
print(tabulate(menuMinuman, tablefmt="grid", headers=[
      "No.", "Menu Minuman", "Tarif"], numalign="center", stralign="center"))
print("\n Menu Tambahan")
print(tabulate(menuTambahan, tablefmt="grid", headers=[
      "Pilihan", "Menu Tambahan", "Tarif"], numalign="center", stralign="center"))
print("\t")


def pesanan():

    # Percabangan Menu Makanan
    nama_pelanggan = input("Masukkan Nama Pelanggan: ")
    kode_makanan = input("Masukkan Kode Makanan: ")
    if kode_makanan == "1":
        Makanan = (menuMakanan[0][1])
        tarif_makanan = (hargaMakanan[0])
    elif kode_makanan == "2":
        Makanan = (menuMakanan[1][1])
        tarif_makanan = (hargaMakanan[1])
    elif kode_makanan == "3":
        Makanan = (menuMakanan[2][1])
        tarif_makanan = (hargaMakanan[2])
    elif kode_makanan == "4":
        Makanan = (menuMakanan[3][1])
        tarif_makanan = (hargaMakanan[3])
    elif kode_makanan == "5":
        Makanan = (menuMakanan[4][1])
        tarif_makanan = (hargaMakanan[4])
    elif kode_makanan == "6":
        Makanan = (menuMakanan[5][1])
        tarif_makanan = (hargaMakanan[5])
    elif kode_makanan == "7":
        Makanan = (menuMakanan[6][1])
        tarif_makanan = (hargaMakanan[6])
    elif kode_makanan == "8":
        Makanan = (menuMakanan[7][1])
        tarif_makanan = (hargaMakanan[7])
    elif kode_makanan == "9":
        Makanan = (menuMakanan[8][1])
        tarif_makanan = (hargaMakanan[8])
    elif kode_makanan == "10":
        Makanan = (menuMakanan[9][1])
        tarif_makanan = (hargaMakanan[9])
    else:
        print("Kode Yang Anda Masukkan Tidak Ada Di Daftar Menu!!")

    # Percabangan Menu Minuman
    kode_minuman = input("Masukkan Kode Minuman: ")
    if kode_minuman == "1":
        Minuman = (menuMinuman[0][1])
        tarif_Minuman = (hargaMinuman[0])
    elif kode_minuman == "2":
        Minuman = (menuMinuman[1][1])
        tarif_Minuman = (hargaMinuman[1])
    elif kode_minuman == "3":
        Minuman = (menuMinuman[2][1])
        tarif_Minuman = (hargaMinuman[2])
    elif kode_minuman == "4":
        Minuman = (menuMinuman[3][1])
        tarif_Minuman = (hargaMinuman[3])
    elif kode_minuman == "5":
        Minuman = (menuMinuman[4][1])
        tarif_Minuman = (hargaMinuman[4])
    elif kode_minuman == "6":
        Minuman = (menuMinuman[5][1])
        tarif_Minuman = (hargaMinuman[5])
    elif kode_minuman == "7":
        Minuman = (menuMinuman[6][1])
        tarif_Minuman = (hargaMinuman[6])
    else:
        print("Kode Yang Anda Masukkan Tidak Ada Di Daftar Menu!!")

    # Percabangan Menu Tambahan
    kode_tambahan = input("Masukkan Kode Menu Tambahan: ")
    print()
    if kode_tambahan == "A":
        Tambahan = (menuTambahan[0][1])
        tarif_Tambahan = (hargaTambahan[0])
    elif kode_tambahan == "B":
        Tambahan = (menuTambahan[1][1])
        tarif_Tambahan = (hargaTambahan[1])
    elif kode_tambahan == "C":
        Tambahan = (menuTambahan[2][1])
        tarif_Tambahan = (hargaTambahan[2])
    elif kode_tambahan == "-":
        Tambahan = "-"
        tarif_Tambahan = (hargaTambahan[3])
    else:
        print("Kode Yang Anda Masukkan Tidak Ada Di Daftar Menu!!")

    # Jumlah Bayar
    jumlah = tarif_makanan + tarif_Minuman + tarif_Tambahan

    # PPN
    ppn = int(jumlah * 0.11)

    # Total Yang harus Di Bayar
    Total_bayar = jumlah + ppn
    total_bayar = "Rp. {:,d}".format(Total_bayar)

    # Output Struk Pembayaran
    print("-------------------------------------------------")
    print("             STRUK PEMBAYARAN CAFE ABC           ")
    print("-------------------------------------------------")
    print("Nama Pelanggan\t\t:", nama_pelanggan)
    print("Kode Makanan\t\t:", kode_makanan)
    print("Nama Makanan\t\t:", Makanan)
    print("Tarif Makanan\t\t: Rp.", format(tarif_makanan, ',d'))
    print("Kode Minuman\t\t:", kode_minuman)
    print("Nama Minuman\t\t:", Minuman)
    print("Tarif Minuman\t\t: Rp.", format(tarif_Minuman, ',d'))
    print("Kode Menu Tambahan\t:", kode_tambahan)
    print("Menu Tambahan\t\t:", Tambahan)
    print("Tarif Menu Tambahan\t: Rp. ", format(tarif_Tambahan, ',d'))
    print("Jumlah Bayar\t\t: Rp. ", format(jumlah, ',d'))
    print("PPN 11%\t\t\t: Rp. ", format(ppn, ',d'))
    print("Total Bayar\t\t: Rp. ", format(Total_bayar, ',d'))
    print("-------------------------------------------------")
    nama.append([
        nama_pelanggan,
        Makanan,
        Minuman,
        Tambahan,
        total_bayar
    ])


pesanan()


# fungsi untuk menampilkan table output
def data():
    nomor_tabel = 1
    data_dengan_nomor = [[str(nomor_tabel)] + data for nomor_tabel,
                         data in enumerate(nama, start=1)]
    print(tabulate(data_dengan_nomor, headers=["No", "Nama Pelanggan", "Makanan",
          "Minuman", "Menu Tambahan", "Total Bayar"], tablefmt="fancy_grid"))


data()


# fungsi untuk mencari data pelanggan
def Pencarian(nama, val):
    hasil_pencarian = []
    for data in nama:
        if val.lower() in data[0].lower():
            hasil_pencarian.append(data)
    return hasil_pencarian


# fungsi untuk memilih menu
def menu_transaksi():
    print()
    print("-------------------------------------------------")
    print("                     MENU                        ")
    print("-------------------------------------------------")
    print("[1] Tambahkan Pesanan ")
    print("[2] Lihat Daftar Pembayaran ")
    print("[3] Cari Daftar Pembayaran ")
    print("[4] Exit")
    print("-------------------------------------------------")

    menu = int(input("Pilih Menu : "))
    print("\n")

    # Percabangan untuk memilih menu
    if menu == 1:
        pesanan()
    elif menu == 2:
        data()
    elif menu == 3:
        nomor_tabel = 1
        nama_pesanan = input("Nama Pelanggan: ")
        hasil_pencarian = Pencarian(nama, nama_pesanan)
        print(tabulate(hasil_pencarian, headers=[
              "Nama Pelanggan", "Makanan", "Minuman", "Menu Tambahan", "Total Bayar"], tablefmt="fancy_grid"))
        cari_pesanan.extend(hasil_pencarian)
    elif menu == 4:
        exit()
    else:
        print("Pilihan Yang Anda Pilih Tidak Ada Di Menu!!")


if __name__ == "__main__":
    while (True):
        menu_transaksi()
